import os
import re
from pathlib import Path

import click
import gradio as gr
import huggingface_hub

import groovy as gv


@click.group()
def cli():
    pass


@cli.command()
def publish():
    """Publish a Groovy flow as a Gradio app"""
    click.echo(
        "This will create a new app.py file in the current directory and publish to Hugging Face Spaces\n"
    )
    flow_path = click.prompt(
        "Path to flow file in current directory", default="flow.py"
    )
    flow_name = click.prompt(
        "Name of the variable containing your Flow instance (e.g., 'my_flow' if you have 'my_flow = Flow()')",
        default="flow",
    )
    image_path = click.prompt(
        "Path to image or gif recording in current directory", default="recording.gif"
    )
    publish_all = click.confirm(
        f"Publish entire directory? (If N, only requirements.txt, {image_path}, {flow_path}, and several generated files will be published)",
        default=False,
    )

    # Convert relative path to module path
    module_path = flow_path.replace("/", ".").replace("\\", ".").rstrip(".py")

    # Create the app.py file
    app_content = f"""import gradio as gr
import groovy as gv
from {module_path} import {flow_name}

with gr.Blocks() as app:
    task_box = gr.Textbox(label="🕺 Task", value="{flow_name}.task")
    with gr.Row():
        if {flow_name}.inputs:
            with gr.Column(scale=1):
                for component in {flow_name}.inputs:
                    component.render()
        with gr.Column(scale=2):
            gr.Image(label="Recording", value="{image_path}")

    @gr.on(
        triggers=[app.load] + [input.change for input in {flow_name}.inputs],
        inputs={flow_name}.inputs,
        outputs=[task_box],
        trigger_mode="always_last",
        show_api=False
    )
    def construct_prompt(*input_values):
        return {flow_name}.task.format(*input_values)

    gr.api({flow_name}.to_json, api_name="flow_config")
                

if __name__ == "__main__":
    app.launch()
"""

    with open("app.py", "w") as f:
        f.write(app_content)

    repo_directory = os.getcwd()
    dir_name = os.path.basename(repo_directory)

    hf_api = huggingface_hub.HfApi()
    try:
        whoami = hf_api.whoami()
        if whoami["auth"]["accessToken"]["role"] != "write":
            click.echo("Need 'write' access token to create a Spaces repo.")
            huggingface_hub.login(add_to_git_credential=False)
    except OSError:
        click.echo("Need 'write' access token to create a Spaces repo.")
        huggingface_hub.login(add_to_git_credential=False)

    title = click.prompt("Enter Spaces app title", default=dir_name)
    title = format_title(title)

    click.echo(
        f"\n✨ Created app.py with `{flow_name}` from `{flow_path}`. Publishing..."
    )
    readme_file = os.path.join(repo_directory, "README.md")
    configuration = {
        "title": title,
        "app_file": "app.py",
        "sdk": "gradio",
        "sdk_version": gr.__version__,
        "hardware": "cpu-basic",
        "tags": ["groovy-flow"],
        "flow_file": flow_path,
    }
    huggingface_hub.metadata_save(readme_file, configuration)

    # Create space
    space_id = huggingface_hub.create_repo(
        configuration["title"],
        space_sdk="gradio",
        repo_type="space",
        exist_ok=True,
        space_hardware=configuration["hardware"],
    ).repo_id

    requirements_path = "requirements.txt"
    if not os.path.exists(requirements_path):
        with open(requirements_path, "w") as f:
            f.write(f"groovy=={gv.__version__}\n")

    if publish_all:
        hf_api.upload_folder(
            repo_id=space_id,
            repo_type="space",
            folder_path=repo_directory,
        )
    else:
        files_to_upload = [
            "app.py",
            flow_path,
            "README.md",
            "requirements.txt",
            image_path,
        ]
        for file in files_to_upload:
            hf_api.upload_file(
                repo_id=space_id,
                repo_type="space",
                path_in_repo=file,
                path_or_fileobj=os.path.join(repo_directory, file),
            )

    click.echo(f"\n🚀 Space published at https://huggingface.co/spaces/{space_id}")


def format_title(title: str):
    """Format title to be compatible with Hugging Face Spaces naming requirements"""
    title = title.replace(" ", "_")
    title = re.sub(r"[^a-zA-Z0-9\-._]", "", title)
    title = re.sub("-+", "-", title)
    while title.startswith("."):
        title = title[1:]
    return title


def download_and_run_flow(user_name: str, space_name: str):
    hf_api = huggingface_hub.HfApi()
    hf_api.hf_hub_download(
        repo_id=f"{user_name}/{space_name}",
        repo_type="space",
        local_dir=Path.cwd() / space_name,
        filename="config.json",
    )

    return


@cli.command()
@click.argument("task")
def run(task: str):
    """Launch a Groovy flow with the specified task as a string, or a URL to a Groovy Space"""
    if task.startswith("https://huggingface.co/spaces/"):
        user_name, space_name = task.split("/")[-2:]
        download_and_run_flow(user_name, space_name)
    else:
        flow = gv.Flow(task)
        flow.launch(run_immediately=True)


def main():
    cli()

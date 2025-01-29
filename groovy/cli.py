import click
import os
import re
import huggingface_hub
import gradio as gr

from groovy.flow import Flow


@click.group()
def cli():
    pass


@cli.command()
def publish():
    """Publish a Groovy flow as a Gradio app"""
    click.echo(
        "This will create a new app.py file in the current directory and publish the entire current directory to Hugging Face Spaces\n"
    )
    flow_path = click.prompt("Path to flow file in current directory", default="flow.py")
    flow_name = click.prompt("Name of Flow object in flow file", default="flow")

    # Convert relative path to module path
    module_path = flow_path.replace("/", ".").replace("\\", ".").rstrip(".py")

    # Create the app.py file
    app_content = f"""import gradio as gr
from {module_path} import {flow_name}

with gr.Blocks() as app:
    for component in {flow_name}.inputs:
        component.interactive = True
        component.render()

if __name__ == "__main__":
    app.launch()
"""

    with open("app.py", "w") as f:
        f.write(app_content)

    click.echo(f"✨ Created app.py with {flow_name} from {flow_path}")
    
    # Deploy to Hugging Face Spaces
    repo_directory = os.getcwd()
    dir_name = os.path.basename(repo_directory)
    
    # Login to Hugging Face
    hf_api = huggingface_hub.HfApi()
    try:
        whoami = hf_api.whoami()
        if whoami["auth"]["accessToken"]["role"] != "write":
            click.echo("Need 'write' access token to create a Spaces repo.")
            huggingface_hub.login(add_to_git_credential=False)
    except OSError:
        click.echo("Need 'write' access token to create a Spaces repo.")
        huggingface_hub.login(add_to_git_credential=False)
    
    # Get space title
    title = click.prompt("Enter Spaces app title", default=dir_name)
    title = format_title(title)
    
    # Create/update README with metadata
    readme_file = os.path.join(repo_directory, "README.md")
    configuration = {
        "title": title,
        "app_file": "app.py",
        "sdk": "gradio",
        "sdk_version": gr.__version__,
        "hardware": "cpu-basic"
    }
    huggingface_hub.metadata_save(readme_file, configuration)
    
    # Create and upload to space
    space_id = huggingface_hub.create_repo(
        configuration["title"],
        space_sdk="gradio",
        repo_type="space",
        exist_ok=True,
        space_hardware=configuration["hardware"],
    ).repo_id
    
    hf_api.upload_folder(
        repo_id=space_id,
        repo_type="space",
        folder_path=repo_directory,
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


@cli.command()
@click.argument("task")
def run(task: str):
    """Launch a Groovy flow with the specified task"""
    flow = Flow(task)
    flow.launch(run_immediately=True)


def main():
    cli()

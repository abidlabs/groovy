import click

from groovy.flow import Flow


@click.group()
def cli():
    pass


@cli.command()
def publish():
    """Publish a Groovy flow as a Gradio app"""
    flow_path = click.prompt("Path to flow file", default="flow.py")
    flow_name = click.prompt("Name of Flow object", default="flow")

    # Convert relative path to module path
    module_path = flow_path.replace("/", ".").replace("\\", ".").rstrip(".py")

    # Create the app.py file
    app_content = f"""import gradio as gr
from {module_path} import {flow_name}

with gr.Blocks() as app:
    for component in {flow_name}.input_components:
        component.render()

if __name__ == "__main__":
    app.launch()
"""

    with open("app.py", "w") as f:
        f.write(app_content)

    click.echo(f"✨ Created app.py with {flow_name} from {flow_path}")
    click.echo("Run 'gradio app.py' to launch your app")


@cli.command()
@click.argument("task")
def run(task: str):
    """Launch a Groovy flow with the specified task"""
    flow = Flow(task)
    flow.launch(run_immediately=True)


def main():
    cli()

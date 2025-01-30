<p align="center">
    <a href="https://github.com/abidlabs/groovy/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/abidlabs/groovy.svg?color=blue"></a>
    <a href="https://pypi.org/project/groovy/"><img alt="PyPI" src="https://img.shields.io/pypi/v/groovy"></a>
    <img alt="Python version" src="https://img.shields.io/badge/python-3.10+-important">
</p>


<h1 align="center">🕺 Groovy</h1>

Hi there! This is `groovy`, a Python library that makes it easy to build, debug, and share workflows or _flows_ (e.g. autonomous applications that perform actions using your browser or desktop).

✨ **Build** flows with a simple high-level `Flow` class that can wrap any kind of application. `groovy` is "batteries-included" so you can write your first Flow in just a single line.

🔎 **Debug** flows with an intuitive Gradio user interface, that exposes agent thought while it runs and allows users to "step-in" and intervene at any point.

🤗 **Share** flows on Hugging Face Spaces publicly (or with specific collaborators) and reuse flows from the community


![Screen Recording 2025-01-29 at 1 30 30 AM (online-video-cutter com)](https://github.com/user-attachments/assets/6cb171cd-9a8a-41e2-927c-badf694595d4)

 
## Installation

```bash
$ pip install groovy[full]
```

## Key Features

### 1. Get started immediately ✨

No need for Run instant browser automations with a single command. No need for complex setup or boilerplate code:

```python
groovy flow "find upcoming events in San Francisco related to board games"
```

### 2. Customize Flows

Create interactive automation apps using the `Flow` class. You can define input parameters that users can customize before running the flow:

```python
from groovy import Flow
import gradio as gr

flow = Flow(
    task="Find upcoming events in {} related to {}",
    inputs=[
        gr.Textbox(label="Location", value="San Francisco")
        gr.Textbox(label="Activity", value="board games"),
    ]
)

flow.launch()
```

### 3. Easy Sharing via Hugging Face Spaces

Share your automation workflows with others by publishing to Hugging Face Spaces. Just navigate to your project folder and run:

```bash
groovy publish
```

This will create a public (you can change visibility to private) Hugging Face Space where others can access and use your automation.

### 4. Use Community Workflows

Take advantage of existing workflows created by the community. Run any published workflow locally, e.g.:

```bash
groovy run https://huggingface.co/spaces/abidlabs/Activity_Finder
```


## Roadmap aka leftover TODOs


* Make it easier to modify the default agent
* Allow `task` to be an arbitrary function of inputs, not just a format string
* Add `Flow.run(**input)` which runs the flow programmatically without the Gradio UI
* Add support for `browser-use` and desktop apps
* Make screen recording more robust
* Generally improve troubleshooting

## Contributing

Contributions are welcome! Feel free to submit bug reports and feature requests or submit pull requests


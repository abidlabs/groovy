<p align="center">
    <a href="https://github.com/abidlabs/groovy/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/abidlabs/groovy.svg?color=blue"></a>
    <a href="https://pypi.org/project/groovy/"><img alt="PyPI" src="https://img.shields.io/pypi/v/groovy"></a>
    <img alt="Python version" src="https://img.shields.io/badge/python-3.10+-important">
</p>


<h1 align="center">🕺 Groovy</h1>

`groovy` is a Python library that makes it easy to:

* **build** automation workflows or _flows_ (think: applications that control your browser or desktop)
* **debug** flows with an intuitive Gradio user interface, and 
* **share** flows on Hugging Face Spaces 🤗.

![Screen Recording 2025-01-29 at 1 30 30 AM (online-video-cutter com)](https://github.com/user-attachments/assets/6cb171cd-9a8a-41e2-927c-badf694595d4)

 
## Why?

- **Run quick browser automations** with a single line of code
- **Create automation _functions_** not just one-off tasks that accept user input via a UI and adjust the task accordingly
- **Share workflows easily** via Hugging Face Spaces
- **Reuse existing workflows** from the community 🤗

## Installation

```bash
pip install groovy
```

## Key Features

### 1. One-Line Browser Automation

Run instant browser automations with a single command. No need for complex setup or boilerplate code:

```python
groovy run "find upcoming events in san francisco related to board games"
```

### 2. Build Interactive Apps with Flows

Turn your automation tasks into full-fledged applications using the `Flow` class. Flows let you create interactive interfaces with Gradio components:

```python
from groovy import Flow
import gradio as gr

# Create a Flow with custom input components
flow = Flow(
    task="Search for {query} in {location}",
    inputs=[
        gr.Textbox(label="Search Query"),
        gr.Textbox(label="Location", value="San Francisco")
    ]
)

# Launch the interactive interface
flow.launch()
```

### 3. Easy Sharing via Hugging Face Spaces

Share your automation workflows with others by publishing to Hugging Face Spaces. Just navigate to your project folder and run:

```bash
groovy publish
```

This will create a public URL where others can access and use your automation.

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


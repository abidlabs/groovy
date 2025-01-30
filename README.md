# 🕺 Groovy

`groovy` is a Python library that makes it easy to **build** automation workflows (think: applications that control your browser or desktop), **debug** them with an intuitive Gradio user interface, and **share** them on Hugging Face Spaces 🤗.

![Screen Recording 2025-01-29 at 1 30 30 AM (online-video-cutter com)](https://github.com/user-attachments/assets/6cb171cd-9a8a-41e2-927c-badf694595d4)

Groovy 

## Why Groovy?

- **Run quick browser automations** with a single line of code
- **Create automation apps** with customizable UI components
- **Share workflows easily** via Hugging Face Spaces
- **Reuse existing workflows** from the community

## Installation

```bash
pip install groovy
```

You will also need an `OPENAI_API_KEY` in an `.env` file in the working directory where you run the commands below (TODO: replace with `HF_TOKEN`)

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


## Contributing

Contributions are welcome! Feel free to submit bug reports and feature requests or submit pull requests

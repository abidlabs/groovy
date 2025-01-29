import gradio as gr
from flow import flow

with gr.Blocks() as app:
    for component in flow.inputs:
        component.interactive = True
        component.render()

if __name__ == "__main__":
    app.launch()

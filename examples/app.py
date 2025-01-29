import gradio as gr
import groovy as gv
print(gv.__version__)
from flow import flow

with gr.Blocks() as app:
    task_box = gr.Textbox(label="🕺 Groovy Flow", value="flow.task")
    with gr.Row():
        for component in flow.inputs:
            component.render()

    @gr.on(
        triggers=[app.load] + [input.change for input in flow.inputs],
        inputs=flow.inputs,
        outputs=[prompt_box],
        trigger_mode="always_last",
    )
    def construct_prompt(*input_values):
        return prompt.format(*input_values)
                
    with gr.Row(scale=5):
        gr.Image()

if __name__ == "__main__":
    app.launch()

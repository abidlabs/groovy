import gradio as gr
from flow import flow

with gr.Blocks() as app:
    task_box = gr.Textbox(
        label="🕺 Task",
        value="flow.task",
        info="Run this workflow locally by installing the [Groovy Python package](https://github.com/abidlabs/groovy) and then running `groovy run https://huggingface.co/space/url>`.",
    )
    with gr.Row():
        if flow.inputs:
            with gr.Column(scale=1):
                for component in flow.inputs:
                    component.render()
        with gr.Column(scale=2):
            gr.Image(label="Recording", value="recording.gif")
            config = gr.JSON(visible=False)

    @gr.on(
        triggers=[app.load] + [input.change for input in flow.inputs],
        inputs=flow.inputs,
        outputs=[task_box],
        trigger_mode="always_last",
        show_api=False,
    )
    def construct_prompt(*input_values):
        return flow.task.format(*input_values)

    app.load(flow.to_json, None, config, api_name="flow_config")


if __name__ == "__main__":
    app.launch()

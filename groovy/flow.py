import gradio as gr

from typing import Callable, Sequence
# from groovy.agent import agent_runner

class Flow:
    def __init__(
            self, 
            prompt: str,
            inputs: Sequence[gr.components.Component] | None = None,
            runner: Callable | None = None,
    ):
        self.prompt = prompt
        self.inputs = inputs or []
        self.runner = runner

        with gr.Blocks() as self.app:
            for input in self.inputs:
                input.render()
            
            prompt_box = gr.Textbox(label="Prompt", value=self.prompt)
            run_button = gr.Button("Run", variant="primary")

            @gr.on(triggers=[self.app.load] + [input.change() for input in self.inputs], inputs=self.inputs, outputs=[prompt_box])
            def populate_prompt(*input_values):
                return self.prompt.format(*input_values)

    def launch(self):
        _, self.url, _ = self.app.launch(prevent_thread_lock=True, inline=False, inbrowser=True)
        return self.url
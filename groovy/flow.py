import threading
from typing import Callable, Sequence

import gradio as gr

from groovy.agent import agent_runner

class Flow:
    def __init__(
            self, 
            prompt: str,
            inputs: Sequence[gr.components.Component] | None = None,
            runner: Callable | None = None,
    ):
        self.prompt = prompt
        self.inputs = inputs or []
        self.runner = runner or agent_runner

        with gr.Blocks() as self.app:
            with gr.Tabs() as tabs:
                with gr.Tab("Setup"):
                    for input in self.inputs:
                        input.render()

                    prompt_box = gr.Textbox(label="Prompt", value=self.prompt)
                    run_button = gr.Button("Run", variant="primary")

                    @gr.on(triggers=[self.app.load] + [input.change for input in self.inputs], inputs=self.inputs, outputs=[prompt_box], trigger_mode="always_last")
                    def construct_prompt(*input_values):
                        # run in background thread

                        return self.prompt.format(*input_values)
                    
                with gr.Tab("Flow", id="flow", visible=False) as results_tab:
                    pass

                @gr.on(triggers=[run_button.click], inputs=[prompt_box], outputs=[tabs, results_tab])
                def run_flow(prompt):
                    # run in background thread
                    #     thread = threading.Thread(target=self.runner, args=(prompt,))
                    # thread.start()
                    self.runner(prompt)
                    return gr.Tabs(selected="flow"), gr.Tab(visible=True)


    def launch(self):
        _, self.url, _ = self.app.launch(prevent_thread_lock=True, inline=False, inbrowser=True)
        return self.url
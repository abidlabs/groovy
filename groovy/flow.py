import threading
from typing import Callable, Sequence

import gradio as gr

from groovy.app import create_app
from groovy.agent import agent_runner

class Flow:
    def __init__(
            self, 
            prompt: str,
            inputs: Sequence[gr.components.Component] | None = None,
            runner: Callable | None = None,
            _run_immediately: bool = False,
    ):
        self.prompt = prompt
        self.inputs = inputs or []
        self.runner = runner or agent_runner
        self.app = create_app(self, self.inputs, self.prompt, self.runner, _run_immediately)

    def launch(self):
        _, self.url, _ = self.app.launch(inline=False, inbrowser=True)
        return self.url
from typing import Callable, Sequence

import gradio as gr

from groovy.app import create_app
from groovy.agent import agent_streamer

class Flow:
    def __init__(
            self, 
            prompt: str,
            inputs: Sequence[gr.components.Component] | None = None,
            streamer: Callable | None = None,
            _run_immediately: bool = False,
    ):
        """
        Args:
            prompt: The prompt to run the flow with. Can be a regular string or a format string, in which case the input components' values will be passed to it.
            inputs: The input components whose values will be passed to the prompt.
            streamer: The (generator) function that accepts a formatted prompt strings and streams `str` or `gr.ChatMessage` responses.
            _run_immediately: Whether to run the flow immediately.
        """
        self.prompt = prompt
        self.inputs = inputs or []
        self.streamer = streamer or agent_streamer
        self.app = create_app(self, self.inputs, self.prompt, self.streamer, _run_immediately)

    def launch(self):
        _, self.url, _ = self.app.launch(inline=False, inbrowser=True)
        return self.url
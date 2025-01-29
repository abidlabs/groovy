from collections.abc import Generator
from typing import Callable, Sequence, Union

import gradio as gr

from groovy.agent import browser_agent_streamer
from groovy.app import create_app


class Flow:
    def __init__(
        self,
        task: str,
        inputs: Sequence[gr.components.Component] | None = None,
        stream_fn: Callable[[str], Generator[Union[str, gr.ChatMessage], None, None]]
        | None = None,
        _run_immediately: bool = False,
    ):
        """
        Args:
            task: The task to run. Can be a regular string or a format string, in which case the input components' values will be passed to it.
            inputs: The input components whose values will be passed to the task, if it's a format string.
            stream_fn: The generator function that accepts a task string and yields an arbitrary number of `str`, `PIL.Image`, or `gr.ChatMessage` responses. If not provided, the default streamer (which browses the web to complete a task) will be used.
            _run_immediately: Whether to run the task immediately at .launch() or whether to wait for the user to click the "Run" button in the UI.
        """
        self.task = task
        self.inputs = inputs or []
        self.stream_fn = stream_fn or browser_agent_streamer
        self.app = create_app(
            self, self.inputs, self.task, self.stream_fn, _run_immediately
        )

    def launch(self):
        _, self.url, _ = self.app.launch(inline=False, inbrowser=True)
        return self.url

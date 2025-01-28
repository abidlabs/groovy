import gradio as gr

from typing import Callable, Sequence

class Train:
    def __init__(
            self, 
            fn: Callable,
            inputs: Sequence[gr.Component],
    ):
        self.fn = fn
        self.inputs = inputs

    
import warnings

import gradio as gr
import PIL.Image


class StepMessage:
    """
    An abstract class that represents a message yielded by a step in a flow.

    This is for two purposes:
    1. To provide a common interface for values that should be yielded by a step in a flow
    2. To easily convert values to a gradio ChatMessage object
    """

    def __init__(self, content):
        self.content = content

    def as_chat_message(self) -> gr.ChatMessage:
        pass


class String(StepMessage, str):
    """
    A step message that behaves like a string.
    """

    def as_chat_message(self) -> gr.ChatMessage:
        return gr.ChatMessage(content=self.content, role="assistant")


class Image(StepMessage):
    """
    A step message that contains an PIL Image.
    """

    def __init__(self, image: PIL.Image.Image):
        self.image = image

    def as_chat_message(self) -> gr.ChatMessage:
        return gr.ChatMessage(content=gr.Image(self.image), role="assistant")


def raw_value_to_step_message(value):
    if isinstance(value, str):
        return String(value)
    elif isinstance(value, PIL.Image.Image):
        return Image(value)
    else:
        warnings.warn(f"Unsupported value type: {type(value)}. Will treat as a string.")
        return String(str(value))

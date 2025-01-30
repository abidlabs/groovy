import abc
import gradio as gr 
import PIL.Image
class StepMessage(abc.ABC):
    @abc.abstractmethod
    def as_chat_message(self) -> gr.ChatMessage:
        pass


class String(StepMessage):
    """
    A step message that contains a string.
    """
    def __init__(self, content: str):
        self.content = content

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

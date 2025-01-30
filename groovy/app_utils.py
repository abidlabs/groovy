from PIL import ImageDraw, ImageFont
from PIL.Image import Image

from groovy.utils import open_positioned_browser


def add_step_counter(image: Image, step_number: int) -> Image:
    """Add a step counter to the bottom left of an image.

    Args:
        image: The PIL Image to modify
        step_number: The step number to display

    Returns:
        A new Image with the step counter added
    """
    img_with_text = image.copy()
    draw = ImageDraw.Draw(img_with_text)

    font = ImageFont.load_default().font_variant(size=24)

    step_text = f"Step {step_number}"
    text_bbox = draw.textbbox((0, 0), step_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    padding = 8
    x = padding
    y = img_with_text.height - text_height - padding - 2

    draw.rectangle(
        [
            0,
            img_with_text.height - text_height - padding * 2,
            x + text_width + padding * 2,
            img_with_text.height,
        ],
        fill="#d8b4fe",  # Purple color
        outline="#d8b4fe",
    )

    draw.text((x, y), step_text, fill="black", font=font)

    return img_with_text


if __name__ == "__main__":
    open_positioned_browser("https://www.google.com")
    import time

    time.sleep(3)

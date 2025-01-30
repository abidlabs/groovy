from urllib.parse import urlparse

from screeninfo import get_monitors
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def open_positioned_browser(url, width=200, x=0, y=0):
    """
    Opens Chrome browser with specified width and full height of the primary monitor using Selenium.

    Args:
        url (str): The URL to open
        width (int): Window width in pixels
        x (int): X position on screen
        y (int): Y position on screen
    """
    # Get primary monitor dimensions
    primary_monitor = get_monitors()[0]
    screen_height = primary_monitor.height

    chrome_options = Options()
    chrome_options.add_argument(f"--window-size={width},{screen_height}")
    chrome_options.add_argument(f"--window-position={x},{y}")
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    return driver


if __name__ == "__main__":
    open_positioned_browser("https://www.google.com")
    import time

    time.sleep(3)


def resolve_space_url_to_id(space_url: str) -> str:
    """
    Resolves a Hugging Face space URL to its space ID.

    Parameters:
        space_url (str): The URL of the Hugging Face space
            e.g., 'https://huggingface.co/spaces/abidlabs/examples'
    Returns:
        str: The space ID in the format 'owner/space_name'
            e.g., 'abidlabs/examples'
    Raises:
        ValueError: If the URL is not a valid Hugging Face space URL
        ConnectionError: If there are issues connecting to the Hugging Face API
    """
    parsed_url = urlparse(space_url)
    if parsed_url.netloc not in ["huggingface.co", "www.huggingface.co"]:
        raise ValueError("Not a valid Hugging Face Space URL")
    path_parts = parsed_url.path.strip("/").split("/")
    if len(path_parts) < 3 or path_parts[0] != "spaces":
        raise ValueError("Not a valid Hugging Face Space URL")
    owner = path_parts[1]
    space_name = path_parts[2]
    return f"{owner}/{space_name}"

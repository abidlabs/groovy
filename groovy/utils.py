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
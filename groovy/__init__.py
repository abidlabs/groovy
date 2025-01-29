from pathlib import Path

from groovy.flow import Flow

__version__ = Path(__file__).parent.joinpath("version.txt").read_text().strip()

__all__ = ["Flow", "__version__"]

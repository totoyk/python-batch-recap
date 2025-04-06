from dataclasses import dataclass
from typing import Any


@dataclass
class Sample:
    """
    Sample class to represent a sample in the dataset.
    """
    id: str
    payload: Any

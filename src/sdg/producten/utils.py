from dataclasses import dataclass
from typing import Any


@dataclass
class ProductField:
    name: str
    verbose_name: str
    value: Any
    help_text: str
    is_reference: bool
    is_markdown: bool

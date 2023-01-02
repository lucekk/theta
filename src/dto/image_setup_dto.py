from typing import Optional
from dataclasses import dataclass

@dataclass
class ImageSetupDto:
    max_threshold: int
    min_threshold: int
    max_canny: int
    min_canny: int
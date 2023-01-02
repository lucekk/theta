from typing import Optional
import numpy
from dataclasses import dataclass

@dataclass
class ThetaBasicInfoDto:
    lp: tuple
    rp: tuple
    mp: tuple
    hp: tuple
    x_arr: numpy.ndarray
    axis_slope_value: float
    a_vertical: float
    b_vertical: float
    a_horizontal: float
    b_horizontal: float
    contours: numpy.ndarray
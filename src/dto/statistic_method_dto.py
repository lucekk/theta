from typing import Optional
import numpy
from dataclasses import dataclass

@dataclass
class StatisticMethodDto:
    left_point: tuple
    right_point: tuple
    middle_point: tuple
    high_point: tuple
    x_arr: numpy.ndarray
    left_point_to_draw: tuple
    right_point_to_draw: tuple
    a_horizontal: float
    b_horizontal:float
    angle: tuple
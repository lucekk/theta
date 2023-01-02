import numpy as np
from src.theta_calculator import ThetaCalulcator
from src.dto.theta_basic_info import ThetaBasicInfoDto

class ThetaBasicData:

    def __init__(self, contours, image) -> None:
        self.__contours = contours
        self.__image = image
        self.__left_side_tail = image.shape[1] * 0.05
        self.__right_side_tail = image.shape[1] * 0.95
        self._find_points_to_calculate()

    def _straight_equation(self, pt1, pt2):
        a_compund = (pt1[1]-pt2[1])/(pt1[0]-pt2[0])
        b_compound = (pt1[0] * pt2[1] - pt2[0] * pt1[1]) / (pt1[0] - pt2[0])
        return a_compund, b_compound

    def _find_first_basic_points(self):
        left_side_points = []
        right_side_points = []
        for x in range(len(self.__contours)):
            if x > 1:
                if self.__contours[x][0][1] < self.__contours[x-1][0][1]:
                    approx_high = self.__contours[x][0]
            if self.__contours[x][0][0] < self.__left_side_tail:
                left_side_points.append(self.__contours[x][0])
            if self.__contours[x][0][0] > self.__right_side_tail :
                right_side_points.append(self.__contours[x][0])
        left_axis_point = left_side_points[int(len(left_side_points) * 0.75)]
        right_axis_point = right_side_points[int(len(right_side_points) * 0.75)]        
        return left_axis_point, right_axis_point, approx_high

    def _axis_line_construct(self, shape_dim):
        line_points = []
        line_points_to_x_array = []
        for n in range(3):
            if n == 0:
                for x in range(self.__image.shape[shape_dim]):   
                    line_points_to_x_array.append([[int(x), int(self._a_horiziontal * x + self._b_horizontal)]])
                    line_points.append([int(x), int(self._a_horiziontal * x + self._b_horizontal)])
            else:
                for x in range(self.__image.shape[shape_dim]):
                    line_points.append([int(x), int(self._a_horiziontal * x+self._b_horizontal + n)])
                    line_points.append([int(x), int(self._a_horiziontal * x + self._b_horizontal - n)])
            
        x_arr = np.array(line_points_to_x_array).reshape(len(line_points_to_x_array), 1, 2)

        list_of_axis_points = []        
        for point in self.__contours:
            if list(point[0]) in line_points:
                list_of_axis_points.append(list(point[0]))
        return x_arr, list_of_axis_points

    def _find_points_of_drop(self, list_of_axis_points):
        half_image = self.__image.shape[1]/2
        left_side = []
        right_side = []
        for point in list_of_axis_points:
            dif = half_image - point[0]
            if dif > 0:
                left_side.append(point)
            else:
                right_side.append(point)
                
        lp = (max(left_side))
        rp = (min(right_side))
        mp = (int((lp[0] + rp[0])/2), int((lp[1] + rp[1])/2))
        return lp, rp, mp

    def _axis_slope(self):
        x = self._lp[0]
        y = self._rp[1]
        point_in_stragiht_angle = (x,y)
        axis_slope = ThetaCalulcator().calculate_angle(point_in_stragiht_angle, self._rp, self._lp)
        return axis_slope 

    def _calculate_vertical_straight(self):
        height = ThetaCalulcator().rotate(self._mp, self._rp, -90)
        a_vertical, b_vertical = self._straight_equation(self._mp, height)
        return a_vertical, b_vertical 

    def _find_top_high_point(self, approx_high):
        height_points = []
        for x in range(len(self.__contours)):
            for n in range(2):
                if self.__contours[x][0][1] == approx_high[1] + n:
                    height_points.append(list(self.__contours[x][0]))
        sum_of_y = 0
        for point in height_points:
            sum_of_y += point[1]
        y = sum_of_y/len(height_points) 
        x = (y-self._b_vertical)/self._a_vertical
        return (x,y)

    def _find_points_to_calculate(self):
        left_axis_point, right_axis_point, approx_high = self._find_first_basic_points()
        self._a_horiziontal, self._b_horizontal = self._straight_equation(left_axis_point, right_axis_point)
        self._x_arr, list_of_axis_points = self._axis_line_construct(1)
        self._lp, self._rp, self._mp = self._find_points_of_drop(list_of_axis_points)
        self._axis_slope_value = self._axis_slope()
        self._a_vertical, self._b_vertical = self._calculate_vertical_straight()
        self._hp = self._find_top_high_point(approx_high)

    def get_basic_info_dto(self):
        return ThetaBasicInfoDto(
            self._lp,
            self._rp,
            self._mp, 
            self._hp, 
            self._x_arr, 
            self._axis_slope_value, 
            self._a_vertical, 
            self._b_vertical,
            self._a_horiziontal,
            self._b_horizontal,
            self.__contours
        )
        
        
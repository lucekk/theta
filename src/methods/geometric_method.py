import math
from src.theta_calculator import ThetaCalulcator
from src.dto.geometric_method_dto import GeometricMethodDto
from src.method_factory import Method

class GeometricMethod(Method):

    def __init__(self, theta_basic_info_dto) -> None:
        self.__lp = theta_basic_info_dto.lp
        self.__rp = theta_basic_info_dto.rp
        self.__mp = theta_basic_info_dto.mp
        self.__hp = theta_basic_info_dto.hp
        self.__x_arr = theta_basic_info_dto.x_arr
        self.__axis_slope_value = theta_basic_info_dto.axis_slope_value
        self.__a_vertical = theta_basic_info_dto.a_vertical
        self.__b_vertical = theta_basic_info_dto.b_vertical
        self.__a_horizontal = theta_basic_info_dto.a_horizontal
        self.__b_horizontal = theta_basic_info_dto.b_horizontal
        self.__left_point_to_draw_rotaed, self.__right_point_to_draw_rotaed = self._caluclations()

    def _get_lines_length(self):
        vertical_length = self.__mp[1] - self.__hp[1]
        horizontal_length = (self.__rp[0] - self.__lp[0])/2
        radius = (vertical_length **2 + horizontal_length**2)/(2*vertical_length)
        return radius

    def _get_cenetr_of_circle(self, radius):
        circle_center_y = self.__hp[1] + int(radius)
        circle_center_x = int((circle_center_y -  self.__b_vertical)/ self.__a_vertical)
        return (circle_center_x, circle_center_y)

    def _get_final_angle(self, primal_angle):
        if primal_angle < 0:
            primal_angle = primal_angle + 360
        return primal_angle/2

    def _calculate_points_to_draw(self, side_point, straight_to_draw_lenght, angle):
        x2 = round(side_point[0] + straight_to_draw_lenght * math.cos(math.radians(angle - self.final_angle)))
        y2 = round(side_point[1] + straight_to_draw_lenght * math.sin(math.radians(360 - (180 - self.final_angle))))
        return (x2, y2)

    def _get_data_to_draw(self):
        prop = (self.__rp[0] - self.__lp[0]) - (self.__rp[0] - self.__lp[0]) / ((1 + math.sqrt(5)) / 2)
        straight_to_draw_lenght = round(prop)
        left_point_to_draw = self._calculate_points_to_draw(self.__lp, straight_to_draw_lenght, 360)
        right_point_to_draw = self._calculate_points_to_draw(self.__rp, straight_to_draw_lenght, 180)
        left_point_to_draw_rotaed = ThetaCalulcator.rotate(self.__lp, left_point_to_draw, -self.__axis_slope_value)
        right_point_to_draw_rotaed = ThetaCalulcator.rotate(self.__rp, right_point_to_draw, self.__axis_slope_value)
        return left_point_to_draw_rotaed, right_point_to_draw_rotaed

    def _caluclations(self):
        radius = self._get_lines_length()
        self.__cenetr_of_circle = self._get_cenetr_of_circle(radius)
        primal_angle = ThetaCalulcator.calculate_angle(self.__rp, self.__cenetr_of_circle, self.__lp)
        self.final_angle = self._get_final_angle(primal_angle)
        left_point_to_draw_rotaed, right_point_to_draw_rotaed = self._get_data_to_draw()
        return left_point_to_draw_rotaed, right_point_to_draw_rotaed

    def get_method_data(self):
        return GeometricMethodDto(
            self.__lp,
            self.__rp, 
            self.__mp, 
            self.__hp, 
            self.__x_arr, 
            self.__left_point_to_draw_rotaed, 
            self.__right_point_to_draw_rotaed,
            self.__a_horizontal,
            self.__b_horizontal,
            (self.final_angle, self.final_angle)
        )

        
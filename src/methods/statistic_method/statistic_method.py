import math
from src.methods.method_factory import Method
from src.theta_calculator import ThetaCalulcator
from src.methods.statistic_method.mean_squared_method import MeanSquaredMethod
from src.enum.calculate_point_to_draw_side_enum import CalculatePointToDrawSideEnum
from src.dto.statistic_method_dto import StatisticMethodDto

class StatisticMethod(Method):

    def __init__(self, theta_basic_info_dto, n_points) -> None:
        self.__n_points = n_points * 2
        self.__lp = theta_basic_info_dto.lp
        self.__rp = theta_basic_info_dto.rp
        self.__mp = theta_basic_info_dto.mp
        self.__hp = theta_basic_info_dto.hp
        self.__x_arr = theta_basic_info_dto.x_arr
        self.__a_horizontal = theta_basic_info_dto.a_horizontal
        self.__b_horizontal = theta_basic_info_dto.b_horizontal
        self.__contours = theta_basic_info_dto.contours
        self.__left_angle, self.__right_angle, self.__left_point_to_draw, self.__right_point_to_draw = self._caluclations()

    def _contour_points_to_local_staight(self):
        left_side_points = []
        right_side_points = []
        for x in range(len(self.__contours)):
            if self.__contours[x][0][1] < self.__lp[1] and abs(self.__contours[x][0][0] - self.__lp[0]) <= 50:
                left_side_points.append((self.__contours[x][0][1], self.__contours[x][0][0]))
            elif self.__contours[x][0][1] < self.__rp[1] and abs(self.__contours[x][0][0] - self.__rp[0]) <= 50:
                right_side_points.append((self.__contours[x][0][1], self.__contours[x][0][0]))
        return left_side_points, right_side_points

    def _points_to_find_local_staight(self, left_side_points, right_side_points):
        n_points = self.__n_points
        left_list = ([],[])
        right_list = ([],[])
        while n_points != 0:
            left_reversed_point = left_side_points.pop(left_side_points.index(max(left_side_points)))
            right_reversed_point = right_side_points.pop(right_side_points.index(max(right_side_points)))
            left_list[0].append(left_reversed_point[1])
            left_list[1].append(left_reversed_point[0])
            right_list[0].append(right_reversed_point[1])
            right_list[1].append(right_reversed_point[0])
            if len(left_side_points) == 0 or len(right_side_points) == 0:
                break
            n_points -= 1
        return left_list, right_list

    def _calculate_straight_equation_compounds(self, left_list, right_list):
        left_side_compounds = MeanSquaredMethod(left_list[0], left_list[1])
        right_side_compounds = MeanSquaredMethod(right_list[0], right_list[1])
        alpha_left, beta_left = left_side_compounds.get_alpha_and_beta_to_straight_equation()
        alpha_right, beta_right = right_side_compounds.get_alpha_and_beta_to_straight_equation()
        left_side_mse = left_side_compounds.get_mse()
        right_side_mse = right_side_compounds.get_mse()
        return alpha_left, beta_left, alpha_right, beta_right, left_side_mse, right_side_mse

    def _calclate_bottom_straight_equation_compounds(self):
        alpha_bottom = (self.__lp[1]-self.__rp[1])/(self.__lp[0]-self.__rp[0])
        beta_bottom = (self.__lp[0] * self.__rp[1] - self.__rp[0] * self.__lp[1]) / (self.__lp[0] - self.__rp[0])
        return alpha_bottom, beta_bottom 

    def _calculate_points_to_angle(self, alpha_left, beta_left, alpha_right, beta_right, alpha_bottom, beta_bottom):
        left_point = (self.__lp[0] + 15, beta_left * int(self.__lp[0] + 15) + alpha_left)
        right_point = (self.__rp[0] - 15, beta_right * int(self.__rp[0] - 15) + alpha_right)
        botton_left_point = (self.__lp[0] + 50, alpha_bottom * (self.__lp[0] + 50) + beta_bottom)
        botton_rigth_point = (self.__rp[0] - 50, alpha_bottom * (self.__rp[0] - 50) + beta_bottom)
        return left_point, right_point, botton_left_point, botton_rigth_point

    def _check_angle(self, angle):
        if angle < 0:
            return angle + 180
        return angle

    def _set_start_angle(self, side):
        if side == CalculatePointToDrawSideEnum.LEFT.name:
            return CalculatePointToDrawSideEnum.LEFT.value
        if side == CalculatePointToDrawSideEnum.RIGHT.name:
            return CalculatePointToDrawSideEnum.RIGHT.value

    def _calculate_points_to_draw(self, side_point, straight_to_draw_lenght, side, angle):
        start_angel = self._set_start_angle(side)
        x2 = round(side_point[0] + straight_to_draw_lenght * math.cos(math.radians(start_angel - angle)))
        y2 = round(side_point[1] + straight_to_draw_lenght * math.sin(math.radians(360 - (180 - angle))))
        return (x2, y2)

    def _get_data_to_draw(self, left_angle, right_angle):
        prop = (self.__rp[0] - self.__lp[0]) - (self.__rp[0] - self.__lp[0]) / ((1 + math.sqrt(5)) / 2)
        straight_to_draw_lenght = round(prop)
        left_point_to_draw = self._calculate_points_to_draw(self.__lp, straight_to_draw_lenght, 'LEFT', left_angle)
        right_point_to_draw = self._calculate_points_to_draw(self.__rp, straight_to_draw_lenght, 'RIGHT', right_angle)
        return left_point_to_draw, right_point_to_draw

    def _caluclations(self):
        left_side_points, right_side_points = self._contour_points_to_local_staight()
        left_list, right_list = self._points_to_find_local_staight(left_side_points, right_side_points)
        alpha_left, beta_left, alpha_right, beta_right, left_side_mse, right_side_mse = self._calculate_straight_equation_compounds(left_list, right_list)
        alpha_bottom, beta_bottom = self._calclate_bottom_straight_equation_compounds()
        left_point, right_point, botton_left_point, botton_rigth_point = self._calculate_points_to_angle(alpha_left, beta_left, alpha_right, beta_right, alpha_bottom, beta_bottom)
        left_angle = self._check_angle(ThetaCalulcator.calculate_angle(botton_left_point, self.__lp, left_point))
        right_angle = self._check_angle(ThetaCalulcator.calculate_angle(right_point, self.__rp, botton_rigth_point))
        left_point_to_draw, right_point_to_draw = self._get_data_to_draw(left_angle, right_angle)
        left_angle_with_error = str(round(left_angle, 2)) + f'({round(left_side_mse, 2)})'
        right_angle_with_error = str(round(right_angle, 2)) + f'({round(right_side_mse, 2)})'
        return left_angle_with_error, right_angle_with_error, left_point_to_draw, right_point_to_draw

    def get_method_data(self):
        return StatisticMethodDto(
            self.__lp,
            self.__rp, 
            self.__mp, 
            self.__hp, 
            self.__x_arr, 
            self.__left_point_to_draw, 
            self.__right_point_to_draw,
            self.__a_horizontal,
            self.__b_horizontal,
            (self.__left_angle, self.__right_angle)
        )
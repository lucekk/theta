# -*- coding: utf-8 -*-

import cv2 as cv2
from src.theta_calculator import ThetaCalulcator

class ManualMode:
    
    @staticmethod
    def draw_line(image, left_high, right_high):
        cv2.line(image, (0, abs(left_high)), (image.shape[1] , abs(right_high)), (0, 0, 255), 2)
        cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    @staticmethod
    def draw_vertical_line(image, left_side, right_side):
        cv2.line(image, (left_side, 0), (left_side , 1080), (0, 0, 255), 2)
        cv2.line(image, (right_side, 0), (right_side , 1080), (0, 0, 255), 2)
        cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    @staticmethod
    def find_side_points(value_1, value_2, x1, x2):
        x_list = [x1, x2]
        points_list = []
        a_compund = (value_1 - value_2)/(0 - 2048)
        b_compound = (0 * value_2 - 2048 * value_1) / (0 - 2048)
        for x in x_list:
            points_list.append((x, (round(a_compund * x + b_compound))))
        mp = (int((points_list[0][0] + points_list[1][0])/2), int((points_list[0][1] + points_list[1][1])/2))
        points_list.append(mp)
        return points_list

    @staticmethod
    def draw_line_to_angle(image, pl1, pl2, angle_left, pr1, pr2, angle_right):
        left_angle_to_display, right_angle_to_display = 180 - abs(angle_left), angle_right
        angle_left = abs(angle_left) - 180
        rotated_point_left = ThetaCalulcator.rotate(pl1, pl2, angle_left)
        angle_right = angle_right 
        rotated_point_right = ThetaCalulcator.rotate(pr1, pr2, angle_right)
        cv2.line(image, pl1, rotated_point_left, (0, 0, 255), 2)
        cv2.line(image, pr1, rotated_point_right, (0, 0, 255), 2)
        cv2.putText(image, f"L:{left_angle_to_display}  P:{right_angle_to_display}", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB), left_angle_to_display, right_angle_to_display 


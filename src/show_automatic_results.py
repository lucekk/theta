import cv2 as cv2

class ShowAutomaticResults:

    def __init__(self, method_data_to_draw_and_display_dto, contours, image_copy) -> None:
        self.__contours = contours
        self.__image_copy = image_copy
        self.__angle = method_data_to_draw_and_display_dto.angle
        self.__lp = method_data_to_draw_and_display_dto.left_point
        self.__rp = method_data_to_draw_and_display_dto.right_point
        self.__mp = method_data_to_draw_and_display_dto.middle_point
        self.__hp = method_data_to_draw_and_display_dto.high_point
        self.__x_arr = method_data_to_draw_and_display_dto.x_arr
        self.__a_horizontal = method_data_to_draw_and_display_dto.a_horizontal
        self.__b_horizontal = method_data_to_draw_and_display_dto.b_horizontal
        self.__left_point_to_draw = method_data_to_draw_and_display_dto.left_point_to_draw
        self.__right_point_to_draw = method_data_to_draw_and_display_dto.right_point_to_draw

    def _fixColor(self, image):
        return(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    def show_results(self):
        cv2.drawContours(self.__image_copy, [self.__contours] , 0, (0, 0, 255), 2)
        cv2.line(self.__image_copy, (self.__lp[0] - 3, int(self.__a_horizontal * (self.__lp[0]-3) + self.__b_horizontal)), (self.__left_point_to_draw[0] , self.__left_point_to_draw[1]), (255,255,0), 2)
        cv2.line(self.__image_copy, (self.__rp[0] + 3, int(self.__a_horizontal * (self.__rp[0]-3) + self.__b_horizontal)), (self.__right_point_to_draw[0] , self.__right_point_to_draw[1]), (255,255,0), 2)
        cv2.putText(self.__image_copy, f"L:{round(self.__angle[0])} P:{round(self.__angle[1])}", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.drawContours(self.__image_copy, [self.__x_arr], 0, (255, 255, 0), 2)
        return self._fixColor(self.__image_copy), self.__angle
from src.methods.geometric_method import GeometricMethod
from src.methods.statistic_method import StatisticMethod

class AutomaticCalculations:

    def __init__(self, basic_image_info_dto, method_dto, spinbox_value) -> None:
        self.__method_dto = method_dto
        self.__basic_image_info_dto = basic_image_info_dto
        self._method_data_to_draw_and_display_dto = self._method_switcher(spinbox_value)

    def _method_switcher(self, spinbox_value):
        if self.__method_dto.geometric == True:
            method_dto = GeometricMethod(self.__basic_image_info_dto)
            return method_dto.get_method_data()
        elif self.__method_dto.statistic == True:
            method_dto = StatisticMethod(self.__basic_image_info_dto, spinbox_value)
            return method_dto.get_method_data()

    def get_data_to_draw_and_display(self):
        return self._method_data_to_draw_and_display_dto
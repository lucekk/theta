# This Python file uses the following encoding: utf-8

#pyside6-uic form.ui > ui_mainwindow.py
import cv2 as cv2
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QErrorMessage
from PySide6.QtGui import QPixmap, QImage
from src.ui_mainwindow import Ui_MainWindow
from src.image_processing import ImageProcessing
from src.theta import ThetaBasicData
from src.automatic_caluluations import AutomaticCalculations
from src.manual_mode import ManualMode
from src.dto.image_setup_dto import ImageSetupDto
from src.dto.method_is_boxchecked_dto import MethodIsboxheckedDto
from src.show_automatic_results import ShowAutomaticResults


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._connect_buttons()

    def _connect_buttons(self):
        self.ui.uoload_btn.clicked.connect(self.showImage)
        self.ui.start_btn.clicked.connect(self._start_clicked)
        self.ui.save_btn.clicked.connect(self._save_image)
        self.ui.reset_btn.clicked.connect(self._reset)
        self.ui.verticalSlider1.valueChanged.connect(self._show_lines)
        self.ui.verticalSlider2.valueChanged.connect(self._show_lines)
        self.ui.bottomSlider1.valueChanged.connect(self._show_lines)
        self.ui.bottomSlider2.valueChanged.connect(self._show_lines)
        self.ui.angleSlider1.valueChanged.connect(self._mesure_angle)
        self.ui.angleSlider2.valueChanged.connect(self._mesure_angle)
        self.ui.manualRadioButton.clicked.connect(self._manual_mode_on)

    def showImage(self):
        self.ui.manualRadioButton.setEnabled(True)
        self.ui.save_btn.setEnabled(True)
        self.ui.start_btn.setEnabled(True)
        self.ui.reset_btn.setEnabled(True)
        self.file_path, _ = QFileDialog.getOpenFileName(self, 'Wybierz zdjęcie', r'C:\Users\lucek\OneDrive\Pulpit\THETA\images')
        self.ui.displayImageFile(self.file_path)

    def _set_angle_value(self, angle, method_isboxhecked_dto):
        if method_isboxhecked_dto.geometric == True:
            self.ui.lcdNumber_3.display(angle[0])
        elif method_isboxhecked_dto.statistic == True:
            self.ui.lcdNumber.display((angle[0].split('('))[0])
            self.ui.lcdNumber_2.display((angle[1].split('('))[0])

    def _start_clicked(self):
        image_setup_dto = ImageSetupDto(255, 30, 225, 30)
        try:
            image, contours, image_copy = ImageProcessing(self.file_path, image_setup_dto).get_processed_image()
        except Exception:
            error_dialog = QErrorMessage()
            error_dialog.showMessage('Załaduj plik przed pomiarem!')
        basic_image_info_dto = ThetaBasicData(contours, image).get_basic_info_dto()
        method_isboxhecked_dto = MethodIsboxheckedDto(self.ui.circle_radio_btn.isChecked(), self.ui.lsm_radio_btn.isChecked())
        method_data_to_draw_and_display_dto = AutomaticCalculations(basic_image_info_dto, method_isboxhecked_dto, self.ui.spinBox.value()).get_data_to_draw_and_display()
        image_to_display, angle_to_display = ShowAutomaticResults(method_data_to_draw_and_display_dto, contours, image_copy).show_results()
        self.qimage = QImage(image_to_display, image_to_display.shape[1], image_to_display.shape[0], QImage.Format_RGB888)
        self._set_angle_value(angle_to_display, method_isboxhecked_dto)
        self.ui.displayImageFile(self.qimage)


    def _manual_mode_on(self):
        image_setup_dto = ImageSetupDto(255, 30, 225, 30)
        self.__image, contours, image_copy = ImageProcessing(self.file_path, image_setup_dto).get_processed_image()

    def _show_lines(self):
        image = self.__image.copy()
        self.__image_to_display = ManualMode.draw_line(image, abs(self.ui.verticalSlider1.value()), abs(self.ui.verticalSlider2.value()))
        self.__image_copy = self.__image_to_display.copy()
        self.__image_to_display_with_verticals = ManualMode.draw_vertical_line(self.__image_to_display, self.ui.bottomSlider1.value(), self.ui.bottomSlider2.value())
        self.__points_list = ManualMode.find_side_points(abs(self.ui.verticalSlider1.value()), abs(self.ui.verticalSlider2.value()), self.ui.bottomSlider1.value(), self.ui.bottomSlider2.value())
        self.qimage = QImage(self.__image_to_display_with_verticals, self.__image_to_display.shape[1], self.__image_to_display.shape[0], QImage.Format_RGB888)
        self.ui.displayImageFile(self.qimage)

    def _mesure_angle(self):
        image = self.__image_copy.copy()
        self.__image_to_display_with_angle_line, left_angle_to_display, right_angle_to_display = ManualMode.draw_line_to_angle(image, self.__points_list[0], self.__points_list[2], self.ui.angleSlider1.value(), self.__points_list[1], self.__points_list[2], self.ui.angleSlider2.value())
        self.ui.leftAngleLcdNumber.display(left_angle_to_display)
        self.ui.rightAngleLcdNumber.display(right_angle_to_display)
        self.qimage = QImage(self.__image_to_display_with_angle_line, self.__image_to_display_with_angle_line.shape[1], self.__image_to_display_with_angle_line.shape[0], QImage.Format_RGB888)
        self.ui.displayImageFile(self.qimage)

    def _save_image(self):
        self.file_to_save_path, _ = QFileDialog.getSaveFileName(self, 'Zapisz pomiar', r'C:\Users\lucek\OneDrive\Pulpit\THETA\theta_prototype\results', '*.png')
        self.qimage.save(f'{self.file_to_save_path}')

    def _reset(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._connect_buttons()

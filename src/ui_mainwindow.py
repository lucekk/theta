# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,  
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLCDNumber, QLabel, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QCheckBox ,QSizePolicy,
    QSpinBox, QStatusBar, QVBoxLayout, QWidget, QFileDialog, QSlider)
from superqt import QRangeSlider

from matplotlib import text


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pix_image = QLabel(self.centralwidget)
        self.pix_image.setObjectName(u"pix_image")
        self.pix_image.setGeometry(QRect(210, 10, 950, 540))
        self.pix_image.setPixmap(QPixmap(u"C:\\Users\\lucek\\OneDrive\\Pulpit\\THETA\\theta_prototype\\images\\start_logo5.png"))
        self.uoload_btn = QPushButton(self.centralwidget)
        self.uoload_btn.setObjectName(u"uoload_btn")
        self.uoload_btn.setGeometry(QRect(30, 30, 80, 24))
        self.circle_radio_btn = QRadioButton(self.centralwidget)
        self.circle_radio_btn.setObjectName(u"circle_radio_btn")
        self.circle_radio_btn.setGeometry(QRect(30, 120, 89, 20))
        self.circle_radio_btn.setToolTipDuration(-5)
        self.circle_radio_btn.setChecked(True)
        self.lsm_radio_btn = QRadioButton(self.centralwidget)
        self.lsm_radio_btn.setObjectName(u"lsm_radio_btn")
        self.lsm_radio_btn.setGeometry(QRect(30, 150, 89, 20))
        self.start_btn = QPushButton(self.centralwidget)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setGeometry(QRect(30, 180, 75, 24))
        self.start_btn.setEnabled(False)
        self.save_btn = QPushButton(self.centralwidget)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setGeometry(QRect(26, 560, 83, 24))
        self.save_btn.setEnabled(False)
        self.reset_btn = QPushButton(self.centralwidget)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setGeometry(QRect(30, 590, 75, 24))
        self.reset_btn.setEnabled(False)
        self.lsmwidget = QWidget(self.centralwidget)
        self.lsmwidget.setObjectName(u"lsmwidget")
        self.lsmwidget.setEnabled(True)
        self.lsmwidget.setVisible(False)
        self.lsmwidget.setGeometry(QRect(10, 190, 121, 231))
        self.verticalLayoutWidget = QWidget(self.lsmwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 93, 201))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.spinBox = QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(3)
        self.spinBox.setMaximum(20)

        self.verticalLayout.addWidget(self.spinBox)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.lcdNumber = QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.verticalLayout.addWidget(self.lcdNumber)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.lcdNumber_2 = QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")

        self.verticalLayout.addWidget(self.lcdNumber_2)

        self.circlewidget = QWidget(self.centralwidget)
        self.circlewidget.setObjectName(u"circlewidget")
        self.circlewidget.setEnabled(True)
        self.circlewidget.setGeometry(QRect(10, 190, 120, 80))
        self.verticalLayoutWidget_2 = QWidget(self.circlewidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 20, 79, 52))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.lcdNumber_3 = QLCDNumber(self.verticalLayoutWidget_2)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")
        self.lcdNumber_3.setSegmentStyle(QLCDNumber.Flat)

        self.verticalLayout_2.addWidget(self.lcdNumber_3)

        self.manualRadioButton = QRadioButton(self.centralwidget)
        self.manualRadioButton.setObjectName(u"manualRadioButton")
        self.manualRadioButton.setGeometry(QRect(25, 530, 101, 22))
        self.manualRadioButton.setAutoExclusive(False)
        self.manualRadioButton.setEnabled(False)
        self.manualwidget = QWidget(self.centralwidget)
        self.manualwidget.setObjectName(u"manualwidget")
        self.manualwidget.setEnabled(True)
        self.manualwidget.setVisible(False)
        self.manualwidget.setGeometry(QRect(210, 570, 751, 81))
        self.leftAngleLcdNumber = QLCDNumber(self.centralwidget)
        self.leftAngleLcdNumber.setObjectName(u"leftCannyLcdNumber")
        self.leftAngleLcdNumber.setGeometry(QRect(660, 590, 50, 27))
        self.leftAngleLcdNumber.setSegmentStyle(QLCDNumber.Flat)
        self.leftAngleLcdNumber.setVisible(False)
        self.rightAngleLcdNumber = QLCDNumber(self.centralwidget)
        self.rightAngleLcdNumber.setObjectName(u"leftCannyLcdNumber")
        self.rightAngleLcdNumber.setGeometry(QRect(660, 620, 50, 27))
        self.rightAngleLcdNumber.setSegmentStyle(QLCDNumber.Flat)
        self.rightAngleLcdNumber.setVisible(False)
        self.verticalSlider1 = QSlider(self.centralwidget)
        self.verticalSlider1.setObjectName(u"verticalSlider1")
        self.verticalSlider1.setGeometry(QRect(200, 10, 18, 540))
        self.verticalSlider1.setMinimum(-1080)
        self.verticalSlider1.setMaximum(0)
        self.verticalSlider1.setOrientation(Qt.Vertical)
        self.verticalSlider1.setVisible(False)
        self.verticalSlider2 = QSlider(self.centralwidget)
        self.verticalSlider2.setObjectName(u"verticalSlider2")
        self.verticalSlider2.setGeometry(QRect(1150, 10, 18, 540))
        self.verticalSlider2.setMinimum(-1080)
        self.verticalSlider2.setMaximum(0)
        self.verticalSlider2.setOrientation(Qt.Vertical)
        self.verticalSlider2.setVisible(False)
        self.bottomSlider1 = QSlider(self.centralwidget)
        self.bottomSlider1.setObjectName(u"bottomSlider1")
        self.bottomSlider1.setGeometry(QRect(210, 540, 475, 18))
        self.bottomSlider1.setMinimum(0)
        self.bottomSlider1.setMaximum(1024)
        self.bottomSlider1.setValue(400)
        self.bottomSlider1.setOrientation(Qt.Horizontal)
        self.bottomSlider1.setVisible(False)
        self.bottomSlider2 = QSlider(self.centralwidget)
        self.bottomSlider2.setObjectName(u"bottomSlider2")
        self.bottomSlider2.setGeometry(QRect(685, 540, 475, 18))
        self.bottomSlider2.setMinimum(1025)
        self.bottomSlider2.setMaximum(2048)
        self.bottomSlider2.setValue(1600)
        self.bottomSlider2.setOrientation(Qt.Horizontal)
        self.bottomSlider2.setVisible(False)
        self.angleSlider1 = QSlider(self.centralwidget)
        self.angleSlider1.setObjectName(u"angleSlider1")
        self.angleSlider1.setGeometry(QRect(280, 595, 375, 18))
        self.angleSlider1.setMinimum(-180.00)
        self.angleSlider1.setMaximum(0.00)
        self.angleSlider1.setValue(-90.00)
        self.angleSlider1.setOrientation(Qt.Horizontal)
        self.angleSlider1.setVisible(False)
        self.angleSlider2 = QSlider(self.centralwidget)
        self.angleSlider2.setObjectName(u"angleSlider1")
        self.angleSlider2.setGeometry(QRect(280, 625, 375, 18))
        self.angleSlider2.setMinimum(0)
        self.angleSlider2.setMaximum(180)
        self.angleSlider2.setValue(90)
        self.angleSlider2.setOrientation(Qt.Horizontal)
        self.angleSlider2.setVisible(False)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(210, 590, 60, 30))
        self.label_6.setVisible(False)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(210, 620, 60, 30))
        self.label_7.setVisible(False)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(35, 90, 60, 30))
       


        MainWindow.setCentralWidget(self.centralwidget)
        self.circlewidget.raise_()
        self.lsmwidget.raise_()
        self.pix_image.raise_()
        self.uoload_btn.raise_()
        self.circle_radio_btn.raise_()
        self.lsm_radio_btn.raise_()
        self.start_btn.raise_()
        self.save_btn.raise_()
        self.reset_btn.raise_()
        self.manualRadioButton.raise_()
        self.manualwidget.raise_()
        self.verticalSlider1.raise_()
        self.verticalSlider2.raise_()
        self.bottomSlider1.raise_()
        self.bottomSlider2.raise_()
        self.angleSlider1.raise_()
        self.angleSlider2.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.leftAngleLcdNumber.raise_()
        self.rightAngleLcdNumber.raise_()

        self.retranslateUi(MainWindow)
        self.circle_radio_btn.toggled.connect(self.circlewidget.setVisible)
        self.lsm_radio_btn.toggled.connect(self.lsmwidget.setVisible)
        self.spinBox.valueChanged.connect(MainWindow.update)
        self.manualRadioButton.toggled.connect(self.manualwidget.setVisible)
        self.manualRadioButton.toggled.connect(lambda:self.btnState(self.manualRadioButton))
        self.manualRadioButton.toggled.connect(self.verticalSlider1.setVisible)
        self.manualRadioButton.toggled.connect(self.verticalSlider2.setVisible)
        self.manualRadioButton.toggled.connect(self.bottomSlider1.setVisible)
        self.manualRadioButton.toggled.connect(self.bottomSlider2.setVisible)
        self.manualRadioButton.toggled.connect(self.angleSlider1.setVisible)
        self.manualRadioButton.toggled.connect(self.angleSlider2.setVisible)
        self.manualRadioButton.toggled.connect(self.label_6.setVisible)
        self.manualRadioButton.toggled.connect(self.label_7.setVisible)
        self.manualRadioButton.toggled.connect(self.leftAngleLcdNumber.setVisible)
        self.manualRadioButton.toggled.connect(self.rightAngleLcdNumber.setVisible)

        MainWindow.toolButtonStyleChanged.connect(self.lcdNumber.update)
        
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"THETA", None))
        MainWindow.setWindowIcon(QIcon(u"C:\\Users\\lucek\\OneDrive\\Pulpit\\THETA\\theta_prototype\\images\\logo2.png"))
        self.pix_image.setText("")
        self.uoload_btn.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj plik", None))
        self.circle_radio_btn.setText(QCoreApplication.translate("MainWindow", u"Geo.", None))
        self.lsm_radio_btn.setText(QCoreApplication.translate("MainWindow", u"Stat.", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"Zapisz pomiar", None))
        self.reset_btn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ilo\u015b\u0107 punkt\u00f3w", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"lewy k\u0105t", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"prawy k\u0105t", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"k\u0105t", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", "Lewy kąt", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", "Prawy kąt", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", "Metody", None))
        self.manualRadioButton.setText(QCoreApplication.translate("MainWindow", u"tryb r\u0119czny", None))

    def displayImageFile(self,file_name):
        self.pix_image.setScaledContents(True)
        self.pix_image.setPixmap(QPixmap(file_name))


    def btnState(self, radio_button):
        if radio_button.isChecked() == False:
            self.verticalSlider1.setVisible(False)
            self.verticalSlider2.setVisible(False)
            self.bottomSlider1.setVisible(False)
            self.bottomSlider2.setVisible(False)
            self.angleSlider1.setVisible(False)
            self.angleSlider2.setVisible(False)
            self.label_6.setVisible(False)
            self.label_7.setVisible(False)
            self.leftAngleLcdNumber.setVisible(False)
            self.rightAngleLcdNumber.setVisible(False)

    #def valueSlider (self, display, slider, x):
    #    display.display(slider.value()[x])
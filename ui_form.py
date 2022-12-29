# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QLabel,
    QPushButton, QScrollBar, QSizePolicy, QSlider,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setEnabled(True)
        Widget.resize(321, 332)
        self.formLayout = QFormLayout(Widget)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label, 0, Qt.AlignHCenter)

        self.mode_silent = QPushButton(Widget)
        self.mode_silent.setObjectName(u"mode_silent")

        self.verticalLayout_4.addWidget(self.mode_silent)

        self.mode_default = QPushButton(Widget)
        self.mode_default.setObjectName(u"mode_default")

        self.verticalLayout_4.addWidget(self.mode_default)

        self.mode_power = QPushButton(Widget)
        self.mode_power.setObjectName(u"mode_power")

        self.verticalLayout_4.addWidget(self.mode_power)

        self.mode_turbo = QPushButton(Widget)
        self.mode_turbo.setObjectName(u"mode_turbo")

        self.verticalLayout_4.addWidget(self.mode_turbo)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.verticalLayout_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_cpu_fan = QLabel(Widget)
        self.label_cpu_fan.setObjectName(u"label_cpu_fan")
        self.label_cpu_fan.setMaximumSize(QSize(16777215, 32))

        self.gridLayout.addWidget(self.label_cpu_fan, 0, 2, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_mode = QLabel(Widget)
        self.label_mode.setObjectName(u"label_mode")
        self.label_mode.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_3.addWidget(self.label_mode)

        self.fan_auto = QPushButton(Widget)
        self.fan_auto.setObjectName(u"fan_auto")

        self.verticalLayout_3.addWidget(self.fan_auto)

        self.fan_max = QPushButton(Widget)
        self.fan_max.setObjectName(u"fan_max")

        self.verticalLayout_3.addWidget(self.fan_max)

        self.fan_user = QPushButton(Widget)
        self.fan_user.setObjectName(u"fan_user")

        self.verticalLayout_3.addWidget(self.fan_user)


        self.gridLayout.addLayout(self.verticalLayout_3, 3, 0, 1, 1)

        self.gpu_fan = QScrollBar(Widget)
        self.gpu_fan.setObjectName(u"gpu_fan")
        self.gpu_fan.setOrientation(Qt.Vertical)
        self.gpu_fan.setInvertedAppearance(True)

        self.gridLayout.addWidget(self.gpu_fan, 3, 3, 1, 1, Qt.AlignHCenter)

        self.cpu_fan = QScrollBar(Widget)
        self.cpu_fan.setObjectName(u"cpu_fan")
        self.cpu_fan.setOrientation(Qt.Vertical)
        self.cpu_fan.setInvertedAppearance(True)
        self.cpu_fan.setInvertedControls(True)

        self.gridLayout.addWidget(self.cpu_fan, 3, 2, 1, 1, Qt.AlignHCenter)

        self.label_gpu_fan = QLabel(Widget)
        self.label_gpu_fan.setObjectName(u"label_gpu_fan")

        self.gridLayout.addWidget(self.label_gpu_fan, 0, 3, 1, 1)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.gridLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.rgb_label = QLabel(Widget)
        self.rgb_label.setObjectName(u"rgb_label")
        self.rgb_label.setMaximumSize(QSize(16777215, 32))
        self.rgb_label.setStyleSheet(u"background-color: rgb(128, 128, 128);")
        self.rgb_label.setText(u"")

        self.verticalLayout.addWidget(self.rgb_label)

        self.slider_red = QSlider(Widget)
        self.slider_red.setObjectName(u"slider_red")
        self.slider_red.setTabletTracking(False)
        self.slider_red.setAutoFillBackground(True)
        self.slider_red.setStyleSheet(u"selection-background-color: rgb(250, 20, 20);")
        self.slider_red.setMaximum(255)
        self.slider_red.setSingleStep(16)
        self.slider_red.setValue(128)
        self.slider_red.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.slider_red)

        self.slider_green = QSlider(Widget)
        self.slider_green.setObjectName(u"slider_green")
        self.slider_green.setStyleSheet(u"selection-background-color: rgb(10,255, 10);")
        self.slider_green.setMaximum(255)
        self.slider_green.setSingleStep(16)
        self.slider_green.setValue(128)
        self.slider_green.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.slider_green)

        self.slider_blue = QSlider(Widget)
        self.slider_blue.setObjectName(u"slider_blue")
        self.slider_blue.setStyleSheet(u"selection-background-color: rgb(28, 113, 216);")
        self.slider_blue.setMaximum(255)
        self.slider_blue.setSingleStep(16)
        self.slider_blue.setValue(128)
        self.slider_blue.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.slider_blue)

        self.slider_brightness = QSlider(Widget)
        self.slider_brightness.setObjectName(u"slider_brightness")
        self.slider_brightness.setStyleSheet(u"selection-background-color: rgb(222, 221, 218);")
        self.slider_brightness.setSingleStep(10)
        self.slider_brightness.setValue(50)
        self.slider_brightness.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.slider_brightness)


        self.formLayout.setLayout(1, QFormLayout.SpanningRole, self.verticalLayout)

        self.button_save = QPushButton(Widget)
        self.button_save.setObjectName(u"button_save")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.button_save)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"300se control", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Perfomance Profile", None))
        self.mode_silent.setText(QCoreApplication.translate("Widget", u"Silent", None))
        self.mode_default.setText(QCoreApplication.translate("Widget", u"default", None))
        self.mode_power.setText(QCoreApplication.translate("Widget", u"hi", None))
        self.mode_turbo.setText(QCoreApplication.translate("Widget", u"turbo", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"fan control", None))
        self.label_cpu_fan.setText(QCoreApplication.translate("Widget", u"cpu fan", None))
        self.label_mode.setText(QCoreApplication.translate("Widget", u"Mode", None))
        self.fan_auto.setText(QCoreApplication.translate("Widget", u"auto", None))
        self.fan_max.setText(QCoreApplication.translate("Widget", u"max", None))
        self.fan_user.setText(QCoreApplication.translate("Widget", u"manual", None))
        self.label_gpu_fan.setText(QCoreApplication.translate("Widget", u"gpu fan", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Keyboard Color", None))
        self.button_save.setText(QCoreApplication.translate("Widget", u"save", None))
    # retranslateUi


#!/usr/bin/python
# This Python file uses the following encoding: utf-8
import sys
import logging
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
import json

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QSlider, QScrollBar

import predator_control as hw
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
import ui_form as ui
from ui_form import Ui_Widget


class SettingsSaveMixin():

    def collect_fans(self):
        cp = self.cpu_fan.value()
        gp = self.gpu_fan.value()
        self.settings["fans"]={}
        fans = self.settings["fans"]
        fans["cpu"] = cp
        fans["gpu"] = gp
        fans["mode"] = self.fanmode

    def collect_color(self):
        r = self.slider_red.value()
        g = self.slider_green.value()
        b = self.slider_blue.value()
        brightness = self.slider_brightness.value()  

        self.settings["color"]={}
        settings = self.settings
        settings["color"]["r"]= r
        settings["color"]["g"]= g
        settings["color"]["b"]= b
        settings["color"]["brightness"]= brightness

    def collect_profile(self):
        self.settings["profile"]=self.profile

    def save(self):
        self.settings = {}
        self.collect_fans()
        self.collect_color()
        self.collect_profile()

        with open("config.json","wt") as fp:
            json.dump(self.settings, fp, indent=2)


class SettingsLoadMixin():

    def load(self):
        try:
            with open("config.json","rt") as fp:
                settings = json.load(fp)
        except:
            log.warning("can't find config.json")
            return

        try:
            color = settings["color"]

            self.slider_red.setValue(color["r"])
            self.slider_green.setValue(color["g"])
            self.slider_blue.setValue(color["b"])
            self.slider_brightness.setValue(color["brightness"])
            self.setColor()
        except KeyError:
            log.warning("used color default values")

        try:
            self.set_profile(settings["profile"])
        except KeyError:
            log.warning("use default profile")
            self.set_profile(1)

        try:
            self.set_fanMode(settings["fans"].get("mode",0))
            self.cpu_fan.setValue(settings["fans"].get("cpu",0))
            self.gpu_fan.setValue(settings["fans"].get("gpu",0))
        except KeyError:
            log.warning("used default fan values")


class Widget(QWidget, SettingsSaveMixin, SettingsLoadMixin):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # backlight
        self.slider_red : QSlider = self.ui.slider_red
        self.slider_green : QSlider = self.ui.slider_green
        self.slider_blue : QSlider = self.ui.slider_blue
        self.slider_brightness : QSlider = self.ui.slider_brightness

        self.slider_brightness.valueChanged.connect(self.setColor)
        self.slider_green.valueChanged.connect(self.setColor)
        self.slider_blue.valueChanged.connect(self.setColor)
        self.slider_red.valueChanged.connect(self.setColor)

        # fans
        self.cpu_fan : QScrollBar = self.ui.cpu_fan
        self.gpu_fan : QScrollBar = self.ui.gpu_fan
        self.fan_auto : QPushButton = self.ui.fan_auto
        self.fan_max : QPushButton = self.ui.fan_max
        self.fan_user : QPushButton = self.ui.fan_user

        self.fan_auto.clicked.connect(lambda: self.set_fanMode(0))
        self.fan_user.clicked.connect(lambda: self.set_fanMode(2))
        self.fan_max.clicked.connect(lambda: self.set_fanMode(1))

        self.cpu_fan.valueChanged.connect(self.fanControl)
        self.gpu_fan.valueChanged.connect(self.fanControl)

        # power profiles    
        self.mode_powersave : QPushButton = self.ui.mode_silent
        self.mode_default : QPushButton = self.ui.mode_default
        self.mode_power : QPushButton = self.ui.mode_power
        self.mode_turbo : QPushButton = self.ui.mode_turbo

        self.mode_powersave.clicked.connect(lambda: self.set_profile(0))
        self.mode_default.clicked.connect(lambda: self.set_profile(1))
        self.mode_power.clicked.connect(lambda: self.set_profile(2))
        self.mode_turbo.clicked.connect(lambda: self.set_profile(3))

        self.button_save : QPushButton = self.ui.button_save
        self.button_save.clicked.connect(self.save)
        self.load()

    def set_fanMode(self, mode):
        self.fanmode = mode
        modes = {
            0: hw.fan_auto,
            2: hw.fan_manual,
            1: hw.fan_max}
        modes[mode]()

    def set_profile(self, profile):
        self.profile = profile
        hw.set_profile(profile)

    def fanControl(self):
        cp = self.cpu_fan.value()
        gp = self.gpu_fan.value()
        hw.set_cpufan(cp)
        hw.set_gpufan(gp)

    def setColor(self):
        r = self.slider_red.value()
        g = self.slider_green.value()
        b = self.slider_blue.value()
        brightness = self.slider_brightness.value()
        self.ui.rgb_label.setStyleSheet(f"background-color: rgb({r},{g},{b});")
        hw.set_color(r, g, b, brightness)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()

    log.warning("start")
    hw.start()
    return_code = app.exec()
    sys.exit(return_code)


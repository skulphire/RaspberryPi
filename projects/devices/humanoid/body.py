from __future__ import division
import time
import Adafruit_PCA9685.PCA9685
from drivers.servos.helper import help

class Body(object):
    def __init__(self):
        # top servo controller
        self.tpwm = Adafruit_PCA9685.PCA9685(0x41)
        # bottom servo controller
        self.bpwm = Adafruit_PCA9685.PCA9685(0x40)

        self.tpwm.set_pwm_freq(60)
        self.bpwm.set_pwm_freq(60)

    def waist(self,degrees):
        if degrees == 0:
            self.bpwm.set_pwm(15, 0, 550)
        elif degrees == 90:
            self.bpwm.set_pwm(15,0,350)
        elif degrees == 45:
            self.bpwm.set_pwm(15,0,450)

    def leftThighX(self,degrees):
        if degrees == 0:
            self.bpwm.set_pwm(14,0,500)
        elif degrees == 180:
            self.bpwm.set_pwm(14,0,150)
        elif degrees == 30:
            self.bpwm.set_pwm(14,0,300)

    def rightThighX(self,degrees):
        if degrees == 0:
            self.bpwm.set_pwm(13,0,200)
        elif degrees == 180:
            self.bpwm.set_pwm(13,0,600)
        elif degrees == 30:
            self.bpwm.set_pwm(13,0,500)

    def leftthighY(self,degrees):
        if degrees == 0:
            self.bpwm.set_pwm(0,0,400)

    def rightthighY(self,degrees):
        if degrees == 0:
            self.bpwm.set_pwm(5,0,400)

    def lefthip(self, degrees):
        if degrees == 0:
            self.bpwm.set_pwm(1,0,150)
        elif degrees == 180:
            self.bpwm.set_pwm(1,0,650)


    def righthip(self,degrees):
        if degrees ==0:
            self.bpwm.set_pwm(6,0,500)
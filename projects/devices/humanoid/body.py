from __future__ import division
import time
import Adafruit_PCA9685.PCA9685

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
            self.bpwm.set_pwm(14,0,150)


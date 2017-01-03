from __future__ import division
import time
import Adafruit_PCA9685.PCA9685

class Arms(object):
    def __init__(self):
        #top servo controller
        self.tpwm = Adafruit_PCA9685.PCA9685(0x41)
        #bottom servo controller
        self.bpwm = Adafruit_PCA9685.PCA9685(0x40)

        self.tpwm.set_pwm_freq(60)
        self.bpwm.set_pwm_freq(60)

    def servosOff(self):
        self.tpwm.set_all_pwm(0,0)

    #LEFT ARM
    def leftShoulder(self, degrees):
        if degrees == 0:
            self.tpwm.set_pwm(0, 0, 550)
        elif degrees == 90:
            self.tpwm.set_pwm(0,0,330)
        elif degrees == 180:
            self.tpwm.set_pwm(0, 0, 100)
    def leftElbow(self, degrees):
        if degrees == 0:
            self.tpwm.set_pwm(1, 0, 600)
        elif degrees == 90:
            self.tpwm.set_pwm(1,0,380)
        elif degrees == 180:
            self.tpwm.set_pwm(1, 0, 150)
    def leftHand(self, degrees):
        if degrees == 0:
            self.tpwm.set_pwm(2, 0, 570)
        elif degrees == 90:
            self.tpwm.set_pwm(2,0,330)
        elif degrees == 180:
            self.tpwm.set_pwm(2, 0, 100)

    #RIGHT ARM
    def rightShoulder(self, degrees):
        if degrees == 180:
            self.tpwm.set_pwm(3, 0, 550)
        elif degrees == 90:
            self.tpwm.set_pwm(3,0,330)
        elif degrees == 0:
            self.tpwm.set_pwm(3, 0, 100)
    def rightElbow(self, degrees):
        if degrees == 180:
            self.tpwm.set_pwm(4, 0, 600)
        elif degrees == 90:
            self.tpwm.set_pwm(4,0,380)
        elif degrees == 0:
            self.tpwm.set_pwm(4, 0, 150)
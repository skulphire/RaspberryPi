from __future__ import division
import time
import Adafruit_PCA9685
from drivers.mpu6050.mpudata import MpuData


class servoTest(object):
    def __init__(self):
        self.mpu = MpuData()

        # Initialise the PWM device using the default address
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(60)

        #min,max pulses out of 4096
        self.servoMin = 150
        self.servoMax = 600
        self.xAxis = 0
        self.yAxis = 0
        #self.balance()

    def balance(self):
        while True:
            self.xAxis = self.mpu.getXRotate()
            self.yAxis = self.mpu.getYRotate()
            if (self.yAxis < 0)&(self.yAxis > -30):
                self.pwm.set_pwm(0,0,self.servoMin)
            else:
                self.pwm.set_pwm(0,0,self.servoMax)
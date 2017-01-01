from Adafruit_PWM_Servo_Driver import PWM
from project.drivers.mpu6050.mpudata import MpuData

import time

class servoTest(object):
    def __init__(self):
        self.mpu = MpuData()

        # Initialise the PWM device using the default address
        self.pwm = PWM(0x40)
        self.pwm.setPWMFreq(60)

        #min,max pulses out of 4096
        self.servoMin = 150
        self.servoMax = 600
        self.xAxis = 0
        self.yAxis = 0
        self.balance()

    def balance(self):
        while True:
            self.xAxis = self.mpu.getXRotate()
            self.yAxis = self.mpu.getYRotate()
            if (self.yAxis < 0)&(self.yAxis > -30):
                self.pwm.setPWM(0,0,self.servoMin)
            else:
                self.pwm.setPWM(0,0,self.servoMax)

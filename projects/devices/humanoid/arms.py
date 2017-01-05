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
        self.trsLastPulse = 0

    def servosOff(self):
        self.tpwm.set_all_pwm(0,0)
        self.bpwm.set_all_pwm(0,0)

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

    def testerRightShoulder(self, degrees, speed):
        if speed == 5:
            print("last ", self.trsLastPulse)
            if degrees % 5 == 0:
                pulse = (degrees * 2.5) + 100
                pulse = int(pulse)
                if pulse < self.trsLastPulse:
                    End = pulse - 1
                    to = -25
                else:
                    End = pulse + 1
                    to = 25
                print("end ", End)

                for x in range(self.trsLastPulse, End, to):
                    self.tpwm.set_pwm(3, 0, x)
                    #time.sleep(0.02)
                    print(x)
            self.trsLastPulse = pulse

        elif speed == 4:
            print("last ",self.trsLastPulse)
            if degrees % 5 == 0:
                pulse = (degrees * 2.5) + 100
                pulse = int(pulse)
                if pulse < self.trsLastPulse:
                    End = pulse - 1
                    to = -25
                else:
                    End = pulse + 1
                    to = 25
                print("end ",End)
                for x in range(self.trsLastPulse,End,to):
                    self.tpwm.set_pwm(3,0,x)
                    time.sleep(0.08)
                    print(x)
            self.trsLastPulse = pulse

    def rightElbow(self, degrees):
        if degrees == 180:
            self.tpwm.set_pwm(4, 0, 520)
        elif degrees == 90:
            self.tpwm.set_pwm(4,0,320)
        elif degrees == 0:
            self.tpwm.set_pwm(4, 0, 100)
    def rightHand(self, degrees):
        if degrees == 180:
            self.tpwm.set_pwm(5, 0, 570)
        elif degrees == 90:
            self.tpwm.set_pwm(5,0,350)
        elif degrees == 0:
            self.tpwm.set_pwm(5, 0, 130)
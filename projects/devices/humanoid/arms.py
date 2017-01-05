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
    def leftShoulder(self, degrees,speed):
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
                    time.sleep(0.02)
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

        elif speed == 3:
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
                    time.sleep(0.12)
                    print(x)
            self.trsLastPulse = pulse

    def leftElbow(self, degrees,speed):
        #600-150
        if speed == 5:
            print("last ", self.trsLastPulse)
            if degrees % 5 == 0:
                pulse = (degrees * 2.5) + 150
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
                    time.sleep(0.02)
                    print(x)
            self.trsLastPulse = pulse

        elif speed == 4:
            print("last ",self.trsLastPulse)
            if degrees % 5 == 0:
                pulse = (degrees * 2.5) + 150
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

        elif speed == 3:
            print("last ",self.trsLastPulse)
            if degrees % 5 == 0:
                pulse = (degrees * 2.5) + 150
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
                    time.sleep(0.12)
                    print(x)
            self.trsLastPulse = pulse

    def leftHand(self, degrees, speed):
        #570-100
        #using 550
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
                    time.sleep(0.02)
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

        elif speed == 3:
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
                    time.sleep(0.12)
                    print(x)
            self.trsLastPulse = pulse

    #RIGHT ARM
    def rightShoulder(self, degrees, speed):
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
                    time.sleep(0.02)
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

        elif speed == 3:
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
                    time.sleep(0.12)
                    print(x)
            self.trsLastPulse = pulse

    def rightElbow(self, degrees, speed):
        #520-100
        #using 550
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
                    time.sleep(0.02)
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

        elif speed == 3:
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
                    time.sleep(0.12)
                    print(x)
            self.trsLastPulse = pulse

    def rightHand(self, degrees, speed):
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
                    time.sleep(0.02)
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

        elif speed == 3:
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
                    time.sleep(0.12)
                    print(x)
            self.trsLastPulse = pulse
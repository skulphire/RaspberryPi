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

        self.lsLastPulse = 0
        self.leLastPulse = 0
        self.lhLastPulse = 0

        self.rsLastPulse = 0
        self.reLastPulse = 0
        self.rhLastPulse = 0


    def servosOff(self):
        self.tpwm.set_all_pwm(0,0)
        self.bpwm.set_all_pwm(0,0)

    #LEFT ARM
    def leftShoulder(self, degrees,speed):
        if speed == 5:
            #print("last ", self.rsLastPulse)
            if degrees % 5 == 0:
                pulse = (degrees * 2.5) + 100
                pulse = int(pulse)
                if pulse < self.lsLastPulse:
                    End = pulse - 1
                    to = -25
                else:
                    End = pulse + 1
                    to = 25
             #   print("end ", End)

                for x in range(self.lsLastPulse, End, to):
                    self.tpwm.set_pwm(0, 0, x)
                    time.sleep(0.02)
              #      print(x)
            self.lsLastPulse = pulse

        elif speed == 4:
           # print("last ", self.rsLastPulse)
            if degrees % 5 == 0:
                pulse = (degrees * 2.5) + 100
                pulse = int(pulse)
                if pulse < self.lsLastPulse:
                    End = pulse - 1
                    to = -25
                else:
                    End = pulse + 1
                    to = 25
            #    print("end ",End)
                for x in range(self.lsLastPulse, End, to):
                    self.tpwm.set_pwm(0,0,x)
                    time.sleep(0.08)
             #       print(x)
            self.lsLastPulse = pulse

        elif speed == 3:
            #print("last ", self.rsLastPulse)
            if degrees % 5 == 0:
                pulse = (degrees * 2.5) + 100
                pulse = int(pulse)
                if pulse < self.lsLastPulse:
                    End = pulse - 1
                    to = -25
                else:
                    End = pulse + 1
                    to = 25
                #print("end ",End)
                for x in range(self.lsLastPulse, End, to):
                    self.tpwm.set_pwm(0,0,x)
                    time.sleep(0.12)
                    #print(x)
            self.lsLastPulse = pulse

    def leftElbow(self, degrees,speed):
        #600-150
        if speed == 5:
           # print("last ", self.leLastPulse)
            if degrees % 5 == 0:
                pulse = (degrees * 2.5) + 150
                pulse = int(pulse)
                if pulse < self.leLastPulse:
                    End = pulse - 1
                    to = -25
                else:
                    End = pulse + 1
                    to = 25
            #    print("end ", End)

                for x in range(self.leLastPulse, End, to):
                    self.tpwm.set_pwm(1, 0, x)
                    time.sleep(0.02)
             #       print(x)
            self.leLastPulse = pulse

        elif speed == 4:
            #print("last ", self.leLastPulse)
            if degrees % 5 == 0:
                pulse = (degrees * 2.5) + 150
                pulse = int(pulse)
                if pulse < self.leLastPulse:
                    End = pulse - 1
                    to = -25
                else:
                    End = pulse + 1
                    to = 25
             #   print("end ",End)
                for x in range(self.leLastPulse, End, to):
                    self.tpwm.set_pwm(1,0,x)
                    time.sleep(0.08)
              #      print(x)
            self.leLastPulse = pulse

        elif speed == 3:
            #print("last ", self.rsLastPulse)
            if degrees % 5 == 0:
                pulse = (degrees * 2.5) + 150
                pulse = int(pulse)
                if pulse < self.leLastPulse:
                    End = pulse - 1
                    to = -25
                else:
                    End = pulse + 1
                    to = 25
                #print("end ",End)
                for x in range(self.leLastPulse, End, to):
                    self.tpwm.set_pwm(1,0,x)
                    time.sleep(0.12)
                    #print(x)
            self.leLastPulse = pulse

    def leftHand(self, degrees, speed):
        #570-100
        #using 550
        if speed == 5:
            #print("last ", self.trsLastPulse)
            if degrees % 5 == 0:
                pulse = (degrees * 2.5) + 100
                pulse = int(pulse)
                if pulse < self.lhLastPulse:
                    End = pulse - 1
                    to = -25
                else:
                    End = pulse + 1
                    to = 25
                #print("end ", End)

                for x in range(self.lhLastPulse, End, to):
                    self.tpwm.set_pwm(2, 0, x)
                    time.sleep(0.02)
                    #print(x)
            self.lhLastPulse = pulse

        elif speed == 4:
            #print("last ",self.trsLastPulse)
            if degrees % 5 == 0:
                pulse = (degrees * 2.5) + 100
                pulse = int(pulse)
                if pulse < self.lhLastPulse:
                    End = pulse - 1
                    to = -25
                else:
                    End = pulse + 1
                    to = 25
             #   print("end ",End)
                for x in range(self.lhLastPulse, End, to):
                    self.tpwm.set_pwm(2,0,x)
                    time.sleep(0.08)
              #      print(x)
            self.lhLastPulse = pulse

        elif speed == 3:
            #print("last ",self.trsLastPulse)
            if degrees % 5 == 0:
                pulse = (degrees * 2.5) + 100
                pulse = int(pulse)
                if pulse < self.lhLastPulse:
                    End = pulse - 1
                    to = -25
                else:
                    End = pulse + 1
                    to = 25
             #   print("end ",End)
                for x in range(self.lhLastPulse, End, to):
                    self.tpwm.set_pwm(2,0,x)
                    time.sleep(0.12)
              #      print(x)
            self.lhLastPulse = pulse

    #RIGHT ARM
    def rightShoulder(self, degrees, speed):
        if speed == 5:
            #print("last ", self.trsLastPulse)
            if degrees % 5 == 0:
                pulse = (degrees * 2.5) + 100
                pulse = int(pulse)
                if pulse < self.rsLastPulse:
                    End = pulse - 1
                    to = -25
                else:
                    End = pulse + 1
                    to = 25
             #   print("end ", End)

                for x in range(self.rsLastPulse, End, to):
                    self.tpwm.set_pwm(3, 0, x)
                    time.sleep(0.02)
             #       print(x)
            self.rsLastPulse = pulse

        elif speed == 4:
            print("last ", self.rsLastPulse)
            if degrees % 5 == 0:
                pulse = (degrees * 2.5) + 100
                pulse = int(pulse)
                if pulse < self.rsLastPulse:
                    End = pulse - 1
                    to = -25
                else:
                    End = pulse + 1
                    to = 25
                print("end ",End)
                for x in range(self.rsLastPulse, End, to):
                    self.tpwm.set_pwm(3,0,x)
                    time.sleep(0.08)
                    print(x)
            self.rsLastPulse = pulse

        elif speed == 3:
            print("last ", self.rsLastPulse)
            if degrees % 5 == 0:
                pulse = (degrees * 2.5) + 100
                pulse = int(pulse)
                if pulse < self.rsLastPulse:
                    End = pulse - 1
                    to = -25
                else:
                    End = pulse + 1
                    to = 25
                print("end ",End)
                for x in range(self.rsLastPulse, End, to):
                    self.tpwm.set_pwm(3,0,x)
                    time.sleep(0.12)
                    print(x)
            self.rsLastPulse = pulse

    def rightElbow(self, degrees, speed):
        #520-100
        #using 550
        if speed == 5:
            #print("last ", self.trsLastPulse)
            if degrees % 5 == 0:
                pulse = (degrees * 2.5) + 100
                pulse = int(pulse)
                if pulse < self.reLastPulse:
                    End = pulse - 1
                    to = -25
                else:
                    End = pulse + 1
                    to = 25
             #   print("end ", End)

                for x in range(self.reLastPulse, End, to):
                    self.tpwm.set_pwm(4, 0, x)
                    time.sleep(0.02)
              #      print(x)
            self.reLastPulse = pulse

        elif speed == 4:
            #print("last ",self.trsLastPulse)
            if degrees % 5 == 0:
                pulse = (degrees * 2.5) + 100
                pulse = int(pulse)
                if pulse < self.reLastPulse:
                    End = pulse - 1
                    to = -25
                else:
                    End = pulse + 1
                    to = 25
             #   print("end ",End)
                for x in range(self.reLastPulse, End, to):
                    self.tpwm.set_pwm(4,0,x)
                    time.sleep(0.08)
              #      print(x)
            self.reLastPulse = pulse

        elif speed == 3:
            #print("last ",self.trsLastPulse)
            if degrees % 5 == 0:
                pulse = (degrees * 2.5) + 100
                pulse = int(pulse)
                if pulse < self.reLastPulse:
                    End = pulse - 1
                    to = -25
                else:
                    End = pulse + 1
                    to = 25
             #   print("end ",End)
                for x in range(self.reLastPulse, End, to):
                    self.tpwm.set_pwm(4,0,x)
                    time.sleep(0.12)
              #      print(x)
            self.reLastPulse = pulse

    def rightHand(self, degrees, speed):
        if speed == 5:
            #print("last ", self.trsLastPulse)
            if degrees % 5 == 0:
                pulse = (degrees * 2.5) + 100
                pulse = int(pulse)
                if pulse < self.rhLastPulse:
                    End = pulse - 1
                    to = -25
                else:
                    End = pulse + 1
                    to = 25
             #   print("end ", End)

                for x in range(self.rhLastPulse, End, to):
                    self.tpwm.set_pwm(5, 0, x)
                    time.sleep(0.02)
              #      print(x)
            self.rhLastPulse = pulse

        elif speed == 4:
            #print("last ",self.trsLastPulse)
            if degrees % 5 == 0:
                pulse = (degrees * 2.5) + 100
                pulse = int(pulse)
                if pulse < self.rhLastPulse:
                    End = pulse - 1
                    to = -25
                else:
                    End = pulse + 1
                    to = 25
             #   print("end ",End)
                for x in range(self.rhLastPulse, End, to):
                    self.tpwm.set_pwm(5,0,x)
                    time.sleep(0.08)
             #       print(x)
            self.rhLastPulse = pulse

        elif speed == 3:
            #print("last ",self.trsLastPulse)
            if degrees % 5 == 0:
                pulse = (degrees * 2.5) + 100
                pulse = int(pulse)
                if pulse < self.rhLastPulse:
                    End = pulse - 1
                    to = -25
                else:
                    End = pulse + 1
                    to = 25
             #   print("end ",End)
                for x in range(self.rhLastPulse, End, to):
                    self.tpwm.set_pwm(5,0,x)
                    time.sleep(0.12)
              #      print(x)
            self.rhLastPulse = pulse
from __future__ import division
import time
import Adafruit_PCA9685.PCA9685
from drivers.servos.runservos import RunServos

class Arms(object):
    def __init__(self):
        #top servo controller
        self.tpwm = Adafruit_PCA9685.PCA9685(0x41)
        #bottom servo controller
        self.bpwm = Adafruit_PCA9685.PCA9685(0x40)

        self.tpwm.set_pwm_freq(60)
        self.bpwm.set_pwm_freq(60)

        self.execute = RunServos()

        self.lsLastPulse = 0
        self.leLastPulse = 0
        self.lhLastPulse = 0

        self.rsLastPulse = 0
        self.reLastPulse = 0
        self.rhLastPulse = 0

        self.execute.channels = []
        self.pulsesDict = {}

    def servosOff(self):
        self.tpwm.set_all_pwm(0,0)
        self.bpwm.set_all_pwm(0,0)

    #LEFT ARM
    def leftShoulder(self, degrees,speed):
        if degrees % 5 == 0:
            pulse = (degrees * 2.5) + 100
            pulse = int(pulse)
            if pulse < self.lsLastPulse:
                End = pulse - 1
                step = -25
            else:
                End = pulse + 1
                step = 25

            self.pulsesDict.setdefault(0,[])
            for x in range(self.lsLastPulse, End, step):
                self.pulsesDict[0].append(x)
            self.execute.channels.extend(0)
            self.lsLastPulse = pulse
            self.execute.servos(speed,self.pulsesDict, 2)

    def leftElbow(self, degrees,speed):
        #600-150
        if degrees % 5 == 0:
            pulse = (degrees * 2.5) + 150
            pulse = int(pulse)
            if pulse < self.leLastPulse:
                End = pulse - 1
                step = -25
            else:
                End = pulse + 1
                step = 25
                self.pulsesDict.setdefault(1, [])
                self.execute.channels.extend(1)
            for x in range(self.leLastPulse, End, step):
                self.pulsesDict[1].append(x)
            self.leLastPulse = pulse
            self.execute.servos(speed, self.pulsesDict, 2)

    def leftHand(self, degrees, speed):
        if degrees % 5 == 0:
            pulse = (degrees * 2.5) + 130
            pulse = int(pulse)
            if pulse < self.lhLastPulse:
                End = pulse - 1
                step = -25
            else:
                End = pulse + 1
                step = 25
                self.pulsesDict.setdefault(2, [])
                self.execute.channels.extend(2)
            for x in range(self.lhLastPulse, End, step):
                self.pulsesDict[2].append(x)
            self.lhLastPulse = pulse
            self.execute.servos(speed, self.pulsesDict, 2)

    #RIGHT ARM
    def rightShoulder(self, degrees, speed):
        if degrees % 5 == 0:
            pulse = (degrees * 2.5) + 100
            pulse = int(pulse)
            if pulse < self.rsLastPulse:
                End = pulse - 1
                step = -25
            else:
                End = pulse + 1
                step = 25
                self.pulsesDict.setdefault(3, [])
                self.execute.channels.extend(3)
            for x in range(self.rsLastPulse, End, step):
                self.pulsesDict[3].append(x)
            self.rsLastPulse = pulse
            self.execute.servos(speed, self.pulsesDict, 2)

    def rightElbow(self, degrees, speed):
        if degrees % 5 == 0:
            pulse = (degrees * 2.5) + 100
            pulse = int(pulse)
            if pulse < self.reLastPulse:
                End = pulse - 1
                step = -25
            else:
                End = pulse + 1
                step = 25
                self.pulsesDict.setdefault(4, [])
                self.execute.channels.extend(4)
            for x in range(self.reLastPulse, End, step):
                self.pulsesDict[4].append(x)
            self.reLastPulse = pulse
            self.execute.servos(speed, self.pulsesDict, 2)

    def rightHand(self, degrees, speed):
        if degrees % 5 == 0:
            pulse = (degrees * 2.5) + 130
            pulse = int(pulse)
            if pulse < self.rhLastPulse:
                End = pulse - 1
                step = -25
            else:
                End = pulse + 1
                step = 25
                self.pulsesDict.setdefault(5, [])
                self.execute.channels.extend(5)
            for x in range(self.rhLastPulse, End, step):
                self.pulsesDict[5].append(x)
            self.rhLastPulse = pulse
            self.execute.servos(speed, self.pulsesDict, 2)
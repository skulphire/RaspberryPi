from __future__ import division
import time
from drivers.servos.config import *



class Arms(object):
    def __init__(self):
        self.lsLastPulse = 0
        self.leLastPulse = 0
        self.lhLastPulse = 0

        self.rsLastPulse = 0
        self.reLastPulse = 0
        self.rhLastPulse = 0

        self.pulsesDict = ARMPULSESDICT
        self.channel = CHANNELS
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
            #print("first ",len(CHANNELS))
            self.pulsesDict.setdefault(0,[])
            for x in range(self.lsLastPulse, End, step):
                self.pulsesDict[0].append(x)
            self.channel.append(0)
            self.lsLastPulse = pulse
            CONTROLLER.append(2)
            #servos(speed,self.pulsesDict, 2)

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
            CHANNELS.append(1)
            for x in range(self.leLastPulse, End, step):
                self.pulsesDict[1].append(x)
            self.leLastPulse = pulse
            CONTROLLER.append(2)
            #servos(speed, self.pulsesDict, 2)

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
            CHANNELS.append(2)
            for x in range(self.lhLastPulse, End, step):
                self.pulsesDict[2].append(x)
            self.lhLastPulse = pulse
            CONTROLLER.append(2)
            #servos(speed, self.pulsesDict, 2)

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
            CHANNELS.append(3)
            for x in range(self.rsLastPulse, End, step):
                self.pulsesDict[3].append(x)
            self.rsLastPulse = pulse
            CONTROLLER.append(2)
            #servos(speed, self.pulsesDict, 2)

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
            CHANNELS.append(4)
            for x in range(self.reLastPulse, End, step):
                self.pulsesDict[4].append(x)
            self.reLastPulse = pulse
            CONTROLLER.append(2)
            #servos(speed, self.pulsesDict, 2)

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
            print(len(CHANNELS))
            CHANNELS.append(5)
            for x in range(self.rhLastPulse, End, step):
                self.pulsesDict[5].append(x)
            self.rhLastPulse = pulse
            CONTROLLER.append(2)
            print(len(CHANNELS))
            #servos(speed, self.pulsesDict, 2)
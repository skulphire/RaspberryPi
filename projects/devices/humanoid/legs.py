from __future__ import division
import time
from drivers.servos.config import *

class Legs(object):
    def __init__(self):
        self.pulsesDict = BOTPULSESDICT
        self.rankleY = 0 #5
        self.rankleX = 0 #4
        self.rknee = 0 #3
        self.lankleY = 0 #2
        self.lankleX = 0 #1
        self.lknee = 0 #0

    def leftknee(self,degrees):
        if degrees % 5 == 0:
            pulse = (degrees * 2.5) + 180
            pulse = int(pulse)
            if pulse < self.lknee:
                End = pulse - 1
                step = -25
            else:
                End = pulse + 1
                step = 25
            self.pulsesDict.setdefault(0,[])
            for x in range(self.lknee, End, step):
                self.pulsesDict[0].append(x)
            CHANNELS.append(0)
            self.lknee = pulse
            CONTROLLER.append(1)

    def leftankleY(self,degrees):
        if degrees % 5 == 0:
            pulse = (degrees * 2) + 55
            pulse = int(pulse)
            if pulse < self.lankleY:
                End = pulse - 1
                step = -25
            else:
                End = pulse + 1
                step = 25
            self.pulsesDict.setdefault(2, [])
            for x in range(self.lankleY, End, step):
                self.pulsesDict[2].append(x)
            CHANNELS.append(2)
            self.lankleY = pulse
            CONTROLLER.append(1)

    def leftankleX(self, degrees):
        if degrees % 5 == 0:
            pulse = (degrees * 2) + 150
            pulse = int(pulse)
            if pulse < self.lankleX:
                End = pulse - 1
                step = -25
            else:
                End = pulse + 1
                step = 25
            self.pulsesDict.setdefault(1, [])
            for x in range(self.lankleX, End, step):
                self.pulsesDict[1].append(x)
            CHANNELS.append(1)
            self.lankleX = pulse
            CONTROLLER.append(1)

    def rightknee(self,degrees):
        if degrees % 5 == 0:
            pulse = (degrees * 2.5) + 100
            pulse = int(pulse)
            if pulse < self.rknee:
                End = pulse - 1
                step = -25
            else:
                End = pulse + 1
                step = 25
            self.pulsesDict.setdefault(3,[])
            for x in range(self.rknee, End, step):
                self.pulsesDict[3].append(x)
            CHANNELS.append(3)
            self.rknee = pulse
            CONTROLLER.append(1)

    def rightankleY(self,degrees):
        if degrees % 5 == 0:
            pulse = (degrees * 2.5) + 150
            pulse = int(pulse)
            if pulse < self.rankleY:
                End = pulse - 1
                step = -25
            else:
                End = pulse + 1
                step = 25
            self.pulsesDict.setdefault(5, [])
            for x in range(self.rankleY, End, step):
                self.pulsesDict[5].append(x)
            CHANNELS.append(5)
            self.rankleY = pulse
            CONTROLLER.append(1)

    def rightankleX(self,degrees):
        if degrees % 5 == 0:
            pulse = (degrees * 2) + 50
            pulse = int(pulse)
            if pulse < self.rankleX:
                End = pulse - 1
                step = -25
            else:
                End = pulse + 1
                step = 25
            self.pulsesDict.setdefault(4, [])
            for x in range(self.rankleX, End, step):
                self.pulsesDict[4].append(x)
            CHANNELS.append(4)
            self.rankleX = pulse
            CONTROLLER.append(1)
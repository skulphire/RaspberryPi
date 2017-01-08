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
            pulse = (degrees * 2.5) + 140
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
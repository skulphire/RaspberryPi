from __future__ import division
import time
from drivers.servos.config import *

class Body(object):
    def __init__(self):
        self.pulsesDict = PULSESDICT
        self.wLastPulse = 0 #12
        self.ltxLastPulse = 0 #11
        self.rtxLastPulse = 0 #10
        self.ltyLastPulse = 0 #9
        self.rtyLastPulse = 0 #8
        self.lhipLastPulse = 0 #7
        self.rhipLastPulse = 0 #6



    def waist(self,degrees):
        if degrees % 5 == 0:
            pulse = (degrees * 2.5) + 225
            pulse = int(pulse)
            if pulse < self.wLastPulse:
                End = pulse - 1
                step = -25
            else:
                End = pulse + 1
                step = 25
            self.pulsesDict.setdefault(12,[])
            for x in range(self.wLastPulse, End, step):
                self.pulsesDict[12].append(x)
            CHANNELS.append(12)
            self.wLastPulse = pulse
            CONTROLLER.append(1)


    def rightThighX(self,degrees):
        if degrees % 5 == 0:
            pulse = (degrees * 2.5) + 150
            pulse = int(pulse)
            if pulse < self.ltxLastPulse:
                End = pulse - 1
                step = -25
            else:
                End = pulse + 1
                step = 25
            self.pulsesDict.setdefault(11,[])
            for x in range(self.ltxLastPulse, End, step):
                self.pulsesDict[11].append(x)
            CHANNELS.append(11)
            self.ltxLastPulse = pulse
            CONTROLLER.append(1)

    def rightthighY(self, degrees):
        if degrees % 5 == 0:
            pulse = (degrees * 2.5) + 50
            pulse = int(pulse)
            if pulse < self.rtxLastPulse:
                End = pulse - 1
                step = -25
            else:
                End = pulse + 1
                step = 25
            self.pulsesDict.setdefault(10, [])
            for x in range(self.rtxLastPulse, End, step):
                self.pulsesDict[10].append(x)
            CHANNELS.append(10)
            self.rtxLastPulse = pulse
            CONTROLLER.append(1)

    def righthip(self, degrees):
        if degrees % 5 == 0:
            pulse = (degrees * 2.5) + 50
            pulse = int(pulse)
            if pulse < self.rtxLastPulse:
                End = pulse - 1
                step = -25
            else:
                End = pulse + 1
                step = 25
            self.pulsesDict.setdefault(9, [])
            for x in range(self.rtxLastPulse, End, step):
                self.pulsesDict[9].append(x)
            CHANNELS.append(9)
            self.rtxLastPulse = pulse
            CONTROLLER.append(1)

        #if degrees == 0:
        #    self.bpwm.set_pwm(6, 0, 500)

    def leftThighX(self, degrees):
        if degrees == 0:
            self.bpwm.set_pwm(2, 0, 500)
        elif degrees == 180:
            self.bpwm.set_pwm(2, 0, 150)
        elif degrees == 30:
            self.bpwm.set_pwm(2, 0, 300)
    def leftthighY(self,degrees):
        if degrees == 0:
            self.bpwm.set_pwm(0,0,400)
    def lefthip(self, degrees):
        if degrees == 0:
            self.bpwm.set_pwm(1,0,150)
        elif degrees == 180:
            self.bpwm.set_pwm(1,0,650)

from __future__ import division
import time
import Adafruit_PCA9685.PCA9685
from .config import *



class RunServos(object):
    def __init__(self):

        # top servo controller
        self.tpwm = Adafruit_PCA9685.PCA9685(0x41)
        # bottom servo controller
        self.bpwm = Adafruit_PCA9685.PCA9685(0x40)
        self.tpwm.set_pwm_freq(60)
        self.bpwm.set_pwm_freq(60)
        
        self.commands = 0
        self.c = 0

    def testlist(self,x, pulseDict, channel, lastpulsetop):
        try:
            pulse = pulseDict[channel][x]
            self.last = pulse
        except:
            pulse = lastpulsetop[channel]
            pass
        return pulse

    def dopwm(self,x,pulseDict,lastpulsestop):
        for i in range(0,self.commands):
            pwm = self.checkpwm()
            pwm.set_pwm(CHANNELS[i], 0, self.testlist(x, pulseDict, CHANNELS[i], lastpulsestop))

    def checkpwm(self):
        if self.c < self.commands:
            if CONTROLLER[self.c] == 1:
                pwm = self.bpwm
            elif CONTROLLER[self.c] == 2:
                pwm = self.tpwm
            self.c = self.c + 1
        else:
            self.c = 0
            if CONTROLLER[self.c] == 1:
                pwm = self.bpwm
            elif CONTROLLER[self.c] == 2:
                pwm = self.tpwm
            self.c = self.c + 1
        return pwm

    def servos(self, pulseDict, lastpulsestop):
        self.c = 0
        self.commands = len(CHANNELS)
        #print(self.commands)
        #finds the biggest list in the dictionary
        maxkey = max(pulseDict, key=lambda x: len(set(pulseDict[x])))
        maxlist = len(pulseDict[maxkey])
        for x in range(0, maxlist):
            self.dopwm(x, pulseDict, lastpulsestop)
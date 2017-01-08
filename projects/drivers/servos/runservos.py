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

    def testlist(self, x, toppulseDict, channel, lastpulsetop, lastpulsesbot, i):
        try:
            pulse = toppulseDict[channel][x]
            self.last = pulse
        except:
            if CONTROLLER[i] == 1:
                pulse = lastpulsesbot[channel]
            elif CONTROLLER[i] == 2:
                pulse = lastpulsetop[channel]
            pass
        return pulse

    def dopwm(self, x,botpulseDict ,toppulseDict, lastpulsestop, lastpulsesbot):
        for i in range(0,self.commands):
            pwm,pulsedict = self.checkpwm(toppulseDict,botpulseDict)
            pwm.set_pwm(CHANNELS[i], 0, self.testlist(x, pulsedict, CHANNELS[i], lastpulsestop, lastpulsesbot, i))
            #print(i)

    def checkpwm(self,top,bot):
        if self.c < self.commands:
            if CONTROLLER[self.c] == 1:
                pwm = self.bpwm
                d = bot
            elif CONTROLLER[self.c] == 2:
                pwm = self.tpwm
                d = top
            self.c = self.c + 1
        else:
            self.c = 0
            if CONTROLLER[self.c] == 1:
                pwm = self.bpwm
                d=bot
            elif CONTROLLER[self.c] == 2:
                pwm = self.tpwm
                d=top
            self.c = self.c + 1
        return pwm,d

    def servos(self,botpulseDict ,toppulseDict, lastpulsestop, lastpulsesbot):
        self.c = 0
        self.commands = len(CHANNELS)
        #print(self.commands)
        #finds the biggest list in the dictionary
        maxkey = max(toppulseDict, key=lambda x: len(set(toppulseDict[x])))
        maxlist = len(toppulseDict[maxkey])
        for x in range(0, maxlist):
            self.dopwm(x,botpulseDict ,toppulseDict, lastpulsestop, lastpulsesbot)
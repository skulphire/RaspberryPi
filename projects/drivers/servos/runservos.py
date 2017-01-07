from __future__ import division
import time
import Adafruit_PCA9685.PCA9685
from .helper import *


class RunServos(object):
    def __init__(self):
        # top servo controller
        self.tpwm = Adafruit_PCA9685.PCA9685(0x41)
        # bottom servo controller
        self.bpwm = Adafruit_PCA9685.PCA9685(0x40)
        self.tpwm.set_pwm_freq(60)
        self.bpwm.set_pwm_freq(60)
        self.channels = channels[]
        self.controller = controller[]
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

    def checkpwm(self):
        if self.c < self.commands:
            if self.controller[self.c] == 1:
                pwm = self.bpwm
            elif self.controller[self.c] == 2:
                pwm = self.tpwm
            self.c = self.c + 1
        else:
            self.c = 0
            if self.controller[self.c] == 1:
                pwm = self.bpwm
            elif self.controller[self.c] == 2:
                pwm = self.tpwm
            self.c = self.c + 1
        return pwm

    def servos(self, pulseDict, lastpulsestop):
        self.c = 0
        self.commands = len(self.channels)
        print(self.commands)
        #finds the biggest list in the dictionary
        maxkey = max(pulseDict, key=lambda x: len(set(pulseDict[x])))
        maxlist = len(pulseDict[maxkey])
        if self.commands == 1:
            for x in range(0,maxlist):
                pwm = self.checkpwm()
                pwm.set_pwm(self.channels[0], 0, self.testlist(x, pulseDict, self.channels[0], lastpulsestop))
        elif self.commands == 2:
            for x in range(0,maxlist):
                pwm = self.checkpwm()
                pwm.set_pwm(self.channels[0], 0, self.testlist(x, pulseDict, self.channels[0], lastpulsestop))
                pwm = self.checkpwm()
                pwm.set_pwm(self.channels[1], 0, self.testlist(x, pulseDict, self.channels[1], lastpulsestop))
        elif self.commands == 3:
            for x in range(0, maxlist):
                pwm = self.checkpwm()
                pwm.set_pwm(self.channels[0], 0, self.testlist(x, pulseDict, self.channels[0], lastpulsestop))
                pwm = self.checkpwm()
                pwm.set_pwm(self.channels[1], 0, self.testlist(x, pulseDict, self.channels[1], lastpulsestop))
                pwm = self.checkpwm()
                pwm.set_pwm(self.channels[2], 0, self.testlist(x, pulseDict, self.channels[2], lastpulsestop))
                time.sleep(0.05)
        elif self.commands == 4:
            for x in range(0, maxlist):
                pwm = self.checkpwm()
                pwm.set_pwm(self.channels[0], 0, self.testlist(x, pulseDict, self.channels[0], lastpulsestop))
                pwm = self.checkpwm()
                pwm.set_pwm(self.channels[1], 0, self.testlist(x, pulseDict, self.channels[1], lastpulsestop))
                pwm = self.checkpwm()
                pwm.set_pwm(self.channels[2], 0, self.testlist(x, pulseDict, self.channels[2], lastpulsestop))
                pwm = self.checkpwm()
                pwm.set_pwm(self.channels[3], 0, self.testlist(x, pulseDict, self.channels[3], lastpulsestop))
        elif self.commands == 5:
            for x in range(0, maxlist):
                pwm = self.checkpwm()
                pwm.set_pwm(self.channels[0], 0, self.testlist(x, pulseDict, self.channels[0], lastpulsestop))
                pwm = self.checkpwm()
                pwm.set_pwm(self.channels[1], 0, self.testlist(x, pulseDict, self.channels[1], lastpulsestop))
                pwm = self.checkpwm()
                pwm.set_pwm(self.channels[2], 0, self.testlist(x, pulseDict, self.channels[2], lastpulsestop))
                pwm = self.checkpwm()
                pwm.set_pwm(self.channels[3], 0, self.testlist(x, pulseDict, self.channels[3], lastpulsestop))
                pwm = self.checkpwm()
                pwm.set_pwm(self.channels[4], 0, self.testlist(x, pulseDict, self.channels[4], lastpulsestop))
        elif self.commands == 6:
            for x in range(0, maxlist):
                pwm = self.checkpwm()
                pwm.set_pwm(self.channels[0], 0, self.testlist(x, pulseDict, self.channels[0], lastpulsestop))
                pwm = self.checkpwm()
                pwm.set_pwm(self.channels[1], 0, self.testlist(x, pulseDict, self.channels[1], lastpulsestop))
                pwm = self.checkpwm()
                pwm.set_pwm(self.channels[2], 0, self.testlist(x, pulseDict, self.channels[2], lastpulsestop))
                pwm = self.checkpwm()
                pwm.set_pwm(self.channels[3], 0, self.testlist(x, pulseDict, self.channels[3], lastpulsestop))
                pwm = self.checkpwm()
                pwm.set_pwm(self.channels[4], 0, self.testlist(x, pulseDict, self.channels[4], lastpulsestop))
                pwm = self.checkpwm()
                pwm.set_pwm(self.channels[5], 0, self.testlist(x, pulseDict, self.channels[5], lastpulsestop))

        elif self.commands == 7:
            for x in range(0, maxlist):

                pwm.set_pwm(self.channels[0], 0, self.testlist(x, pulseDict, self.channels[0], lastpulsestop))
                pwm.set_pwm(self.channels[1], 0, self.testlist(x, pulseDict, self.channels[1], lastpulsestop))
                pwm.set_pwm(self.channels[2], 0, self.testlist(x, pulseDict, self.channels[2], lastpulsestop))
                pwm.set_pwm(self.channels[3], 0, self.testlist(x, pulseDict, self.channels[3], lastpulsestop))
                pwm.set_pwm(self.channels[4], 0, self.testlist(x, pulseDict, self.channels[4], lastpulsestop))
                pwm.set_pwm(self.channels[5], 0, self.testlist(x, pulseDict, self.channels[5], lastpulsestop))
                pwm.set_pwm(self.channels[6], 0, self.testlist(x, pulseDict, self.channels[6], lastpulsestop))
        elif self.commands == 8:
            for x in range(0, maxlist):

                pwm.set_pwm(self.channels[0], 0, self.testlist(x, pulseDict, self.channels[0], lastpulsestop))
                pwm.set_pwm(self.channels[1], 0, self.testlist(x, pulseDict, self.channels[1], lastpulsestop))
                pwm.set_pwm(self.channels[2], 0, self.testlist(x, pulseDict, self.channels[2], lastpulsestop))
                pwm.set_pwm(self.channels[3], 0, self.testlist(x, pulseDict, self.channels[3], lastpulsestop))
                pwm.set_pwm(self.channels[4], 0, self.testlist(x, pulseDict, self.channels[4], lastpulsestop))
                pwm.set_pwm(self.channels[5], 0, self.testlist(x, pulseDict, self.channels[5], lastpulsestop))
                pwm.set_pwm(self.channels[6], 0, self.testlist(x, pulseDict, self.channels[6], lastpulsestop))
                pwm.set_pwm(self.channels[7], 0, self.testlist(x, pulseDict, self.channels[7], lastpulsestop))
        elif self.commands == 9:
            for x in range(0, maxlist):

                pwm.set_pwm(self.channels[0], 0, self.testlist(x, pulseDict, self.channels[0], lastpulsestop))
                pwm.set_pwm(self.channels[1], 0, self.testlist(x, pulseDict, self.channels[1], lastpulsestop))
                pwm.set_pwm(self.channels[2], 0, self.testlist(x, pulseDict, self.channels[2], lastpulsestop))
                pwm.set_pwm(self.channels[3], 0, self.testlist(x, pulseDict, self.channels[3], lastpulsestop))
                pwm.set_pwm(self.channels[4], 0, self.testlist(x, pulseDict, self.channels[4], lastpulsestop))
                pwm.set_pwm(self.channels[5], 0, self.testlist(x, pulseDict, self.channels[5], lastpulsestop))
                pwm.set_pwm(self.channels[6], 0, self.testlist(x, pulseDict, self.channels[6], lastpulsestop))
                pwm.set_pwm(self.channels[7], 0, self.testlist(x, pulseDict, self.channels[7], lastpulsestop))
                pwm.set_pwm(self.channels[8], 0, self.testlist(x, pulseDict, self.channels[8], lastpulsestop))
        elif self.commands == 10:
            for x in range(0, maxlist):

                pwm.set_pwm(self.channels[0], 0, self.testlist(x, pulseDict, self.channels[0], lastpulsestop))
                pwm.set_pwm(self.channels[1], 0, self.testlist(x, pulseDict, self.channels[1], lastpulsestop))
                pwm.set_pwm(self.channels[2], 0, self.testlist(x, pulseDict, self.channels[2], lastpulsestop))
                pwm.set_pwm(self.channels[3], 0, self.testlist(x, pulseDict, self.channels[3], lastpulsestop))
                pwm.set_pwm(self.channels[4], 0, self.testlist(x, pulseDict, self.channels[4], lastpulsestop))
                pwm.set_pwm(self.channels[5], 0, self.testlist(x, pulseDict, self.channels[5], lastpulsestop))
                pwm.set_pwm(self.channels[6], 0, self.testlist(x, pulseDict, self.channels[6], lastpulsestop))
                pwm.set_pwm(self.channels[7], 0, self.testlist(x, pulseDict, self.channels[7], lastpulsestop))
                pwm.set_pwm(self.channels[8], 0, self.testlist(x, pulseDict, self.channels[8], lastpulsestop))
                pwm.set_pwm(self.channels[9], 0, self.testlist(x, pulseDict, self.channels[9], lastpulsestop))
        elif self.commands == 11:
            for x in range(0, maxlist):

                pwm.set_pwm(self.channels[0], 0, self.testlist(x, pulseDict, self.channels[0], lastpulsestop))
                pwm.set_pwm(self.channels[1], 0, self.testlist(x, pulseDict, self.channels[1], lastpulsestop))
                pwm.set_pwm(self.channels[2], 0, self.testlist(x, pulseDict, self.channels[2], lastpulsestop))
                pwm.set_pwm(self.channels[3], 0, self.testlist(x, pulseDict, self.channels[3], lastpulsestop))
                pwm.set_pwm(self.channels[4], 0, self.testlist(x, pulseDict, self.channels[4], lastpulsestop))
                pwm.set_pwm(self.channels[5], 0, self.testlist(x, pulseDict, self.channels[5], lastpulsestop))
                pwm.set_pwm(self.channels[6], 0, self.testlist(x, pulseDict, self.channels[6], lastpulsestop))
                pwm.set_pwm(self.channels[7], 0, self.testlist(x, pulseDict, self.channels[7], lastpulsestop))
                pwm.set_pwm(self.channels[8], 0, self.testlist(x, pulseDict, self.channels[8], lastpulsestop))
                pwm.set_pwm(self.channels[9], 0, self.testlist(x, pulseDict, self.channels[9], lastpulsestop))
                pwm.set_pwm(self.channels[10], 0, self.testlist(x, pulseDict, self.channels[10], lastpulsestop))
        elif self.commands == 12:
            for x in range(0, maxlist):

                pwm.set_pwm(self.channels[0], 0, self.testlist(x, pulseDict, self.channels[0], lastpulsestop))
                pwm.set_pwm(self.channels[1], 0, self.testlist(x, pulseDict, self.channels[1], lastpulsestop))
                pwm.set_pwm(self.channels[2], 0, self.testlist(x, pulseDict, self.channels[2], lastpulsestop))
                pwm.set_pwm(self.channels[3], 0, self.testlist(x, pulseDict, self.channels[3], lastpulsestop))
                pwm.set_pwm(self.channels[4], 0, self.testlist(x, pulseDict, self.channels[4], lastpulsestop))
                pwm.set_pwm(self.channels[5], 0, self.testlist(x, pulseDict, self.channels[5], lastpulsestop))
                pwm.set_pwm(self.channels[6], 0, self.testlist(x, pulseDict, self.channels[6], lastpulsestop))
                pwm.set_pwm(self.channels[7], 0, self.testlist(x, pulseDict, self.channels[7], lastpulsestop))
                pwm.set_pwm(self.channels[8], 0, self.testlist(x, pulseDict, self.channels[8], lastpulsestop))
                pwm.set_pwm(self.channels[9], 0, self.testlist(x, pulseDict, self.channels[9], lastpulsestop))
                pwm.set_pwm(self.channels[10], 0, self.testlist(x, pulseDict, self.channels[10], lastpulsestop))
                pwm.set_pwm(self.channels[11], 0, self.testlist(x, pulseDict, self.channels[11], lastpulsestop))
        elif self.commands == 13:
            for x in range(0, maxlist):

                pwm.set_pwm(self.channels[0], 0, self.testlist(x, pulseDict, self.channels[0], lastpulsestop))
                pwm.set_pwm(self.channels[1], 0, self.testlist(x, pulseDict, self.channels[1], lastpulsestop))
                pwm.set_pwm(self.channels[2], 0, self.testlist(x, pulseDict, self.channels[2], lastpulsestop))
                pwm.set_pwm(self.channels[3], 0, self.testlist(x, pulseDict, self.channels[3], lastpulsestop))
                pwm.set_pwm(self.channels[4], 0, self.testlist(x, pulseDict, self.channels[4], lastpulsestop))
                pwm.set_pwm(self.channels[5], 0, self.testlist(x, pulseDict, self.channels[5], lastpulsestop))
                pwm.set_pwm(self.channels[6], 0, self.testlist(x, pulseDict, self.channels[6], lastpulsestop))
                pwm.set_pwm(self.channels[7], 0, self.testlist(x, pulseDict, self.channels[7], lastpulsestop))
                pwm.set_pwm(self.channels[8], 0, self.testlist(x, pulseDict, self.channels[8], lastpulsestop))
                pwm.set_pwm(self.channels[9], 0, self.testlist(x, pulseDict, self.channels[9], lastpulsestop))
                pwm.set_pwm(self.channels[10], 0, self.testlist(x, pulseDict, self.channels[10], lastpulsestop))
                pwm.set_pwm(self.channels[11], 0, self.testlist(x, pulseDict, self.channels[11], lastpulsestop))
                pwm.set_pwm(self.channels[12], 0, self.testlist(x, pulseDict, self.channels[12], lastpulsestop))
        del self.channels[:]
        self.channels = []
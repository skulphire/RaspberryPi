from __future__ import division
import time
import Adafruit_PCA9685.PCA9685


class RunServos(object):
    def __init__(self):
        # top servo controller
        self.tpwm = Adafruit_PCA9685.PCA9685(0x41)
        # bottom servo controller
        self.bpwm = Adafruit_PCA9685.PCA9685(0x40)
        self.tpwm.set_pwm_freq(60)
        self.bpwm.set_pwm_freq(60)
        self.channels =[]

    def testlist(self,x, pulseDict, channel):
        try:
            pulse = pulseDict[channel][x]
        except:
            pulse = pulseDict[channel][x-1]
            pass
        return pulse
    def servos(self ,speed, pulseDict,controller):
        commands = len(self.channels)
        if controller == 1:
            pwm = self.bpwm
        elif controller == 2:
            pwm = self.tpwm
        #finds the biggest list in the dictionary
        maxkey = max(pulseDict, key=lambda x: len(set(pulseDict[x])))
        maxlist = len(pulseDict[maxkey])
        if commands == 1:
            print("here1")
            for x in range(0,maxlist):
                pwm.set_pwm(self.channels[0],0,pulseDict[self.channels[0]][x])
        elif commands == 2:
            print("here")
            for x in range(0,maxlist):
                pwm.set_pwm(self.channels[0],0,self.testlist(x,pulseDict,self.channels[0]))
                pwm.set_pwm(self.channels[1], 0, self.testlist(x,pulseDict,self.channels[1]))
        elif commands == 3:
            for x in range(0, maxlist):
                pwm.set_pwm(self.channels[0], 0, self.testlist(x, pulseDict, self.channels[0]))
                pwm.set_pwm(self.channels[1], 0, self.testlist(x, pulseDict, self.channels[1]))
                pwm.set_pwm(self.channels[2], 0, self.testlist(x, pulseDict, self.channels[2]))
        elif commands == 4:
            for x in range(0, maxlist):
                pwm.set_pwm(self.channels[0], 0, self.testlist(x, pulseDict, self.channels[0]))
                pwm.set_pwm(self.channels[1], 0, self.testlist(x, pulseDict, self.channels[1]))
                pwm.set_pwm(self.channels[2], 0, self.testlist(x, pulseDict, self.channels[2]))
                pwm.set_pwm(self.channels[3], 0, self.testlist(x, pulseDict, self.channels[3]))
        elif commands == 5:
            for x in range(0, maxlist):
                pwm.set_pwm(self.channels[0], 0, self.testlist(x, pulseDict, self.channels[0]))
                pwm.set_pwm(self.channels[1], 0, self.testlist(x, pulseDict, self.channels[1]))
                pwm.set_pwm(self.channels[2], 0, self.testlist(x, pulseDict, self.channels[2]))
                pwm.set_pwm(self.channels[3], 0, self.testlist(x, pulseDict, self.channels[3]))
                pwm.set_pwm(self.channels[4], 0, self.testlist(x, pulseDict, self.channels[4]))
        elif commands == 6:
            for x in range(0, maxlist):
                pwm.set_pwm(self.channels[0], 0, self.testlist(x, pulseDict, self.channels[0]))
                pwm.set_pwm(self.channels[1], 0, self.testlist(x, pulseDict, self.channels[1]))
                pwm.set_pwm(self.channels[2], 0, self.testlist(x, pulseDict, self.channels[2]))
                pwm.set_pwm(self.channels[3], 0, self.testlist(x, pulseDict, self.channels[3]))
                pwm.set_pwm(self.channels[4], 0, self.testlist(x, pulseDict, self.channels[4]))
                pwm.set_pwm(self.channels[5], 0, self.testlist(x, pulseDict, self.channels[5]))
        elif commands == 7:
            for x in range(0, maxlist):
                pwm.set_pwm(self.channels[0], 0, self.testlist(x, pulseDict, self.channels[0]))
                pwm.set_pwm(self.channels[1], 0, self.testlist(x, pulseDict, self.channels[1]))
                pwm.set_pwm(self.channels[2], 0, self.testlist(x, pulseDict, self.channels[2]))
                pwm.set_pwm(self.channels[3], 0, self.testlist(x, pulseDict, self.channels[3]))
                pwm.set_pwm(self.channels[4], 0, self.testlist(x, pulseDict, self.channels[4]))
                pwm.set_pwm(self.channels[5], 0, self.testlist(x, pulseDict, self.channels[5]))
                pwm.set_pwm(self.channels[6], 0, self.testlist(x, pulseDict, self.channels[6]))
        elif commands == 8:
            for x in range(0, maxlist):
                pwm.set_pwm(self.channels[0], 0, self.testlist(x, pulseDict, self.channels[0]))
                pwm.set_pwm(self.channels[1], 0, self.testlist(x, pulseDict, self.channels[1]))
                pwm.set_pwm(self.channels[2], 0, self.testlist(x, pulseDict, self.channels[2]))
                pwm.set_pwm(self.channels[3], 0, self.testlist(x, pulseDict, self.channels[3]))
                pwm.set_pwm(self.channels[4], 0, self.testlist(x, pulseDict, self.channels[4]))
                pwm.set_pwm(self.channels[5], 0, self.testlist(x, pulseDict, self.channels[5]))
                pwm.set_pwm(self.channels[6], 0, self.testlist(x, pulseDict, self.channels[6]))
                pwm.set_pwm(self.channels[7], 0, self.testlist(x, pulseDict, self.channels[7]))
        elif commands == 9:
            for x in range(0, maxlist):
                pwm.set_pwm(self.channels[0], 0, self.testlist(x, pulseDict, self.channels[0]))
                pwm.set_pwm(self.channels[1], 0, self.testlist(x, pulseDict, self.channels[1]))
                pwm.set_pwm(self.channels[2], 0, self.testlist(x, pulseDict, self.channels[2]))
                pwm.set_pwm(self.channels[3], 0, self.testlist(x, pulseDict, self.channels[3]))
                pwm.set_pwm(self.channels[4], 0, self.testlist(x, pulseDict, self.channels[4]))
                pwm.set_pwm(self.channels[5], 0, self.testlist(x, pulseDict, self.channels[5]))
                pwm.set_pwm(self.channels[6], 0, self.testlist(x, pulseDict, self.channels[6]))
                pwm.set_pwm(self.channels[7], 0, self.testlist(x, pulseDict, self.channels[7]))
                pwm.set_pwm(self.channels[8], 0, self.testlist(x, pulseDict, self.channels[8]))
        elif commands == 10:
            for x in range(0, maxlist):
                pwm.set_pwm(self.channels[0], 0, self.testlist(x, pulseDict, self.channels[0]))
                pwm.set_pwm(self.channels[1], 0, self.testlist(x, pulseDict, self.channels[1]))
                pwm.set_pwm(self.channels[2], 0, self.testlist(x, pulseDict, self.channels[2]))
                pwm.set_pwm(self.channels[3], 0, self.testlist(x, pulseDict, self.channels[3]))
                pwm.set_pwm(self.channels[4], 0, self.testlist(x, pulseDict, self.channels[4]))
                pwm.set_pwm(self.channels[5], 0, self.testlist(x, pulseDict, self.channels[5]))
                pwm.set_pwm(self.channels[6], 0, self.testlist(x, pulseDict, self.channels[6]))
                pwm.set_pwm(self.channels[7], 0, self.testlist(x, pulseDict, self.channels[7]))
                pwm.set_pwm(self.channels[8], 0, self.testlist(x, pulseDict, self.channels[8]))
                pwm.set_pwm(self.channels[9], 0, self.testlist(x, pulseDict, self.channels[9]))
        elif commands == 11:
            for x in range(0, maxlist):
                pwm.set_pwm(self.channels[0], 0, self.testlist(x, pulseDict, self.channels[0]))
                pwm.set_pwm(self.channels[1], 0, self.testlist(x, pulseDict, self.channels[1]))
                pwm.set_pwm(self.channels[2], 0, self.testlist(x, pulseDict, self.channels[2]))
                pwm.set_pwm(self.channels[3], 0, self.testlist(x, pulseDict, self.channels[3]))
                pwm.set_pwm(self.channels[4], 0, self.testlist(x, pulseDict, self.channels[4]))
                pwm.set_pwm(self.channels[5], 0, self.testlist(x, pulseDict, self.channels[5]))
                pwm.set_pwm(self.channels[6], 0, self.testlist(x, pulseDict, self.channels[6]))
                pwm.set_pwm(self.channels[7], 0, self.testlist(x, pulseDict, self.channels[7]))
                pwm.set_pwm(self.channels[8], 0, self.testlist(x, pulseDict, self.channels[8]))
                pwm.set_pwm(self.channels[9], 0, self.testlist(x, pulseDict, self.channels[9]))
                pwm.set_pwm(self.channels[10], 0, self.testlist(x, pulseDict, self.channels[10]))
        elif commands == 12:
            for x in range(0, maxlist):
                pwm.set_pwm(self.channels[0], 0, self.testlist(x, pulseDict, self.channels[0]))
                pwm.set_pwm(self.channels[1], 0, self.testlist(x, pulseDict, self.channels[1]))
                pwm.set_pwm(self.channels[2], 0, self.testlist(x, pulseDict, self.channels[2]))
                pwm.set_pwm(self.channels[3], 0, self.testlist(x, pulseDict, self.channels[3]))
                pwm.set_pwm(self.channels[4], 0, self.testlist(x, pulseDict, self.channels[4]))
                pwm.set_pwm(self.channels[5], 0, self.testlist(x, pulseDict, self.channels[5]))
                pwm.set_pwm(self.channels[6], 0, self.testlist(x, pulseDict, self.channels[6]))
                pwm.set_pwm(self.channels[7], 0, self.testlist(x, pulseDict, self.channels[7]))
                pwm.set_pwm(self.channels[8], 0, self.testlist(x, pulseDict, self.channels[8]))
                pwm.set_pwm(self.channels[9], 0, self.testlist(x, pulseDict, self.channels[9]))
                pwm.set_pwm(self.channels[10], 0, self.testlist(x, pulseDict, self.channels[10]))
                pwm.set_pwm(self.channels[11], 0, self.testlist(x, pulseDict, self.channels[11]))
        elif commands == 13:
            for x in range(0, maxlist):
                pwm.set_pwm(self.channels[0], 0, self.testlist(x, pulseDict, self.channels[0]))
                pwm.set_pwm(self.channels[1], 0, self.testlist(x, pulseDict, self.channels[1]))
                pwm.set_pwm(self.channels[2], 0, self.testlist(x, pulseDict, self.channels[2]))
                pwm.set_pwm(self.channels[3], 0, self.testlist(x, pulseDict, self.channels[3]))
                pwm.set_pwm(self.channels[4], 0, self.testlist(x, pulseDict, self.channels[4]))
                pwm.set_pwm(self.channels[5], 0, self.testlist(x, pulseDict, self.channels[5]))
                pwm.set_pwm(self.channels[6], 0, self.testlist(x, pulseDict, self.channels[6]))
                pwm.set_pwm(self.channels[7], 0, self.testlist(x, pulseDict, self.channels[7]))
                pwm.set_pwm(self.channels[8], 0, self.testlist(x, pulseDict, self.channels[8]))
                pwm.set_pwm(self.channels[9], 0, self.testlist(x, pulseDict, self.channels[9]))
                pwm.set_pwm(self.channels[10], 0, self.testlist(x, pulseDict, self.channels[10]))
                pwm.set_pwm(self.channels[11], 0, self.testlist(x, pulseDict, self.channels[11]))
                pwm.set_pwm(self.channels[12], 0, self.testlist(x, pulseDict, self.channels[12]))
        self.channels = []

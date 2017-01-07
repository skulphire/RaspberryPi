from __future__ import division
import time
import Adafruit_PCA9685.PCA9685
#from devices.humanoid.arms import Arms
#from devices.humanoid.body import Body

class RunServos(object):
    def __init__(self):
        # top servo controller
        self.tpwm = Adafruit_PCA9685.PCA9685(0x41)
        # bottom servo controller
        self.bpwm = Adafruit_PCA9685.PCA9685(0x40)
        self.tpwm.set_pwm_freq(60)
        self.bpwm.set_pwm_freq(60)
        self.channels = []
        #self.arm = Arms()
        #self.body = Body()

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
            for x in range(0,maxlist):
                pwm.set_pwm(self.channels[0],0,pulseDict[self.channels[0]][x])
        elif commands == 2:
            for x in range(0,maxlist):
                pwm.set_pwm(self.channels[0],0,self.testlist(x,pulseDict,self.channels[0]))
                pwm.set_pwm(self.channels[1], 0, self.testlist(x,pulseDict,self.channels[1]))
        elif commands == 3:
            for x in range(0,maxlist):
                try:
                    p1 = pulseDict[self.channels[0]][x]
                except:
                    pass
                try:
                    p2 = pulseDict[self.channels[0]][x]
                except:
                    pass
                try:
                    p3 = pulseDict[self.channels[0]][x]
                except:
                    pass
                pwm.set_pwm(self.channels[0],0,p1)
                pwm.set_pwm(self.channels[1], 0, p2)
                pwm.set_pwm(self.channels[2], 0, p3)
        elif commands == 4:
            for x in range(0, maxlist):
                try:
                    p1 = pulseDict[self.channels[0]][x]
                except:
                    pass
                try:
                    p2 = pulseDict[self.channels[0]][x]
                except:
                    pass
                try:
                    p3 = pulseDict[self.channels[0]][x]
                except:
                    pass
                try:
                    p4 = pulseDict[self.channels[0]][x]
                except:
                    pass
                pwm.set_pwm(self.channels[0], 0, p1)
                pwm.set_pwm(self.channels[1], 0, p2)
                pwm.set_pwm(self.channels[2], 0, p3)
        self.channels = []

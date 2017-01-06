from __future__ import division
import time
import Adafruit_PCA9685.PCA9685
from devices.humanoid.arms import Arms
from devices.humanoid.body import Body

class RunServos(object):
    def __init__(self):
        # top servo controller
        self.tpwm = Adafruit_PCA9685.PCA9685(0x41)
        # bottom servo controller
        self.bpwm = Adafruit_PCA9685.PCA9685(0x40)
        self.tpwm.set_pwm_freq(60)
        self.bpwm.set_pwm_freq(60)

        self.arm = Arms()
        self.body = Body()

    def servos(self ,speed, pulses, channels,controller, to):
        commands = len(channels)
        if controller == 1:
            pwm = self.bpwm
        elif controller == 2:
            pwm = self.tpwm

        if commands == 1:
            pwm.set_pwm(channels(0),0,)
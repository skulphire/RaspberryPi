import time
import Adafruit_PCA9685.PCA9685

class Arms(object):
    def __init__(self):
        self.pwm = Adafruit_PCA9685.PCA9685(0x41)
        self.pwm.set_pwm_freq(60)


    def leftShoulder(self, degrees):
        if degrees == 0:
            self.pwm.set_pwm(15,0,150)
        elif degrees == 180:
            self.pwm.set_pwm(15,0,600)

from __future__ import division
import time
from devices.humanoid.arms import Arms

class Pos(object):
    def __init__(self):
        self.arm = Arms()

    def stop(self):
        time.sleep(3)
        self.arm.servosOff()

    def initial(self):
        # standard position:
        self.arm.leftShoulder(0)
        self.arm.leftElbow(0)
        self.arm.leftHand(90)

        self.arm.rightShoulder(0)
        self.arm.rightElbow(0)
        self.arm.rightHand(90)
from __future__ import division
import time
from devices.humanoid.arms import Arms
from devices.humanoid.body import Body

class Pos(object):
    def __init__(self):
        self.arm = Arms()
        self.body = Body()

        #time.sleep(0.3)

    def stop(self):
        #time.sleep(3)
        self.arm.servosOff()
    def initial(self):
        # standard position:
        self.arm.leftShoulder(180,5)
        self.arm.leftElbow(180,5)
        self.arm.leftHand(90,5)

        self.arm.rightShoulder(0,5)
        self.arm.rightElbow(0,5)
        self.arm.rightHand(90,5)

        self.body.waist(45)
        self.body.leftThighX(30)
        self.body.rightThighX(30)
        self.body.leftthighY(0)
        self.body.rightthighY(0)
        self.body.lefthip(0)
        self.body.righthip(0)

    #method for falling backwards
    def fallingBack(self):
        self.arm.leftShoulder(90)
        self.arm.rightShoulder(90)
        self.arm.leftElbow(180)
        self.arm.rightElbow(180)

    def lookLeft(self):
        self.body.waist(90)

    def lookRight(self):
        self.body.waist(0)

    def lookForward(self):
        self.body.waist(45)
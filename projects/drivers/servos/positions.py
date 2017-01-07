from __future__ import division
import time
from devices.humanoid.arms import Arms
from devices.humanoid.body import Body
from drivers.servos.runservos import RunServos

class Pos(object):
    def __init__(self):
        self.arm = Arms()
        self.body = Body()
        self.execute = RunServos()

        #time.sleep(0.3)

    def commit(self):
        lastpulses = [ self.arm.lsLastPulse,
        self.arm.leLastPulse,
        self.arm.lhLastPulse,
        self.arm.rsLastPulse,
        self.arm.reLastPulse,
        self.arm.rhLastPulse]

        self.execute.servos(self.arm.pulsesDict,lastpulses)
        self.arm.pulsesDict.clear()

    def stop(self):
        #time.sleep(3)
        self.arm.servosOff()
    def initial(self):
        # standard position:
        self.arm.leftShoulder(45,5)
        self.arm.leftElbow(135,5)
        self.arm.leftHand(180,5)
        print(len(self.execute.channels))
        #self.arm.rightShoulder(0,5)
        #self.arm.rightElbow(135,5)
        #self.arm.rightHand(180,5)
        self.commit()

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
    def new(self):
        self.arm.leftShoulder(180,5)
        self.arm.rightShoulder(0,5)
        self.arm.leftShoulder(120, 5)
        self.arm.rightShoulder(60, 5)
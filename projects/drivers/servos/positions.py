from __future__ import division
import time
from devices.humanoid.arms import Arms
from devices.humanoid.body import Body
from .runservos import RunServos
from .config import *

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

        ARMPULSESDICT.clear()
        CHANNELS[:] = []
        CONTROLLER[:] = []



    def stop(self):
        self.execute.tpwm.set_all_pwm(0,0)
        self.execute.bpwm.set_all_pwm(0,0)

    def dance1(self):
        self.arm.leftShoulder(180, 5)
        self.arm.leftElbow(90, 5)
        self.arm.leftHand(0, 5)

        self.arm.rightShoulder(0, 5)
        self.arm.rightElbow(90, 5)
        self.arm.rightHand(0, 5)
        self.commit()
        for x in range(0,5):
            self.arm.leftShoulder(180, 5)
            self.arm.leftElbow(90, 5)
            self.arm.leftHand(70, 5)

            self.arm.rightShoulder(0, 5)
            self.arm.rightElbow(90, 5)
            self.arm.rightHand(70, 5)
            self.commit()

            self.arm.leftShoulder(180, 5)
            self.arm.leftElbow(90, 5)
            self.arm.leftHand(0, 5)

            self.arm.rightShoulder(0, 5)
            self.arm.rightElbow(90, 5)
            self.arm.rightHand(0, 5)
            self.commit()

    def initial(self):
        # standard position:
        self.arm.leftShoulder(135,5)
        self.arm.leftElbow(150,5)
        self.arm.leftHand(135,5)

        self.arm.rightShoulder(45,5)
        self.arm.rightElbow(30,5)
        self.arm.rightHand(45,5)
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
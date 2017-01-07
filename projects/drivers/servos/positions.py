from __future__ import division
import time
from devices.humanoid.arms import Arms
from devices.humanoid.body import Body
from devices.humanoid.legs import Legs
from .runservos import RunServos
from .config import *

class Pos(object):
    def __init__(self):
        self.arm = Arms()
        self.body = Body()
        self.legs = Legs()
        self.execute = RunServos()
        #time.sleep(0.3)

    def commit(self):

        lastpulsestop = [ self.arm.lsLastPulse,
        self.arm.leLastPulse,
        self.arm.lhLastPulse,
        self.arm.rsLastPulse,
        self.arm.reLastPulse,
        self.arm.rhLastPulse]

        lastpulsesbot = [self.legs.lknee,self.legs.lankleX,self.legs.lankleY,
                         self.legs.rknee,self.legs.rankleX,self.legs.rankleY,
                         self.body.rhipLastPulse,self.body.lhipLastPulse,self.body.rtyLastPulse,
                         self.body.ltyLastPulse,self.body.rtxLastPulse,self.body.ltxLastPulse,self.body.wLastPulse]

        self.execute.servos(PULSESDICT,lastpulsestop, lastpulsesbot)

        PULSESDICT.clear()
        CHANNELS[:] = []
        CONTROLLER[:] = []



    def stop(self):
        self.execute.tpwm.set_all_pwm(0,0)
        self.execute.bpwm.set_all_pwm(0,0)

    def dance1(self):
        self.arm.leftShoulder(180, 5)
        self.arm.leftElbow(0, 5)
        self.arm.leftHand(180, 5)

        self.arm.rightShoulder(0, 5)
        self.arm.rightElbow(0, 5)
        self.arm.rightHand(180, 5)
        self.commit()
        time.sleep(.5)

        for x in range(0,5):
            self.arm.leftShoulder(180, 5)
            self.arm.leftElbow(0, 5)
            self.arm.leftHand(180, 5)

            self.arm.rightShoulder(0, 5)
            self.arm.rightElbow(0, 5)
            self.arm.rightHand(180, 5)
            self.commit()
            time.sleep(.1)
            self.arm.leftShoulder(180, 5)
            self.arm.leftElbow(60, 5)
            self.arm.leftHand(135, 5)

            self.arm.rightShoulder(0, 5)
            self.arm.rightElbow(60, 5)
            self.arm.rightHand(135, 5)
            self.commit()
            time.sleep(.1)

    def initial(self):
        # standard position:
        self.arm.leftShoulder(135,5)
        self.arm.leftElbow(145,5)
        self.arm.leftHand(135,5)

        self.arm.rightShoulder(45,5)
        self.arm.rightElbow(30,5)
        self.arm.rightHand(45,5)

        self.body.waist(90)
        self.commit()


        #self.body.leftThighX(30)
        #self.body.rightThighX(30)
        #self.body.leftthighY(0)
        #self.body.rightthighY(0)
        #self.body.lefthip(0)
        #self.body.righthip(0)

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
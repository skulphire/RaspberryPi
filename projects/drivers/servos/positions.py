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
                         self.body.lhipLastPulse,self.body.ltyLastPulse,self.body.ltxLastPulse,
                         self.body.rhipLastPulse,self.body.rtyLastPulse,self.body.rtxLastPulse,self.body.wLastPulse]

        self.execute.servos(BOTPULSESDICT, TOPPULSESDICT, lastpulsestop, lastpulsesbot)
        TOPPULSESDICT.clear()
        BOTPULSESDICT.clear()
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

    def standing(self):
        self.arm.leftShoulder(135,5)
        self.arm.leftElbow(145,5)
        self.arm.leftHand(135,5)

        self.arm.rightShoulder(45,5)
        self.arm.rightElbow(30,5)
        self.arm.rightHand(45,5)

        self.body.waist(90)

        self.body.rightThighX(150)
        self.body.rightthighY(150)
        #self.body.righthip(180)
        self.body.righthip(90)

        self.body.leftThighX(150)
        self.body.leftthighY(25)
        self.body.lefthip(0)

        self.legs.leftknee(125)
        self.legs.leftankleY(85)
        self.legs.leftankleX(0)

        self.legs.rightknee(60)
        self.legs.rightankleY(90)
        #self.legs.rightankleX(150)
        self.legs.rightankleX(90)
        self.commit()

    def initial(self):
        # standard position:
        self.arm.leftShoulder(135,5)
        self.arm.leftElbow(145,5)
        self.arm.leftHand(135,5)

        self.arm.rightShoulder(45,5)
        self.arm.rightElbow(30,5)
        self.arm.rightHand(45,5)

        self.body.waist(90)

        self.body.rightThighX(150)
        self.body.rightthighY(180)
        #self.body.rightthighY(150)
        self.body.righthip(180)

        self.body.leftThighX(150)
        self.body.leftthighY(0)
        #self.body.leftthighY(30)
        self.body.lefthip(0)

        self.commit()


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
        #self.body.righthip(0)
        #self.body.rightthighY(0)
        self.legs.rightknee(0)
        self.legs.rightankleY(0)
        self.legs.rightankleX(0)

        #self.body.lefthip(0)
        #self.body.leftthighY(0)
        self.legs.leftknee(0)

        self.commit()
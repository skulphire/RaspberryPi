from drivers.mpu6050.mpudata import MpuData
from drivers.servos.servomputrans import Translator
from drivers.humanoid.arms import Arms
import time

#usefull commands
#i2cdetect -y 1

if __name__ == '__main__':
    arm = Arms()

    #standard position:
    arm.leftHand(90)
    arm.leftElbow(0)
    arm.leftShoulder(0)

    arm.rightShoulder(0)
    arm.rightElbow(90)
    arm.rightHand(90)


    time.sleep(3)
    arm.servosOff()
    #servo = Translator()
    #servo.balance()

#    mpu = MpuData()
#    mpu.turnOn(0x68)
#    while True:
#        mpu.printValues('b')
#        time.sleep(0.5)

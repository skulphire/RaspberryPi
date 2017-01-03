from drivers.mpu6050.mpudata import MpuData
from drivers.servos.servomputrans import Translator
from drivers.humanoid.arms import Arms
import time

#usefull commands
#i2cdetect -y 1

if __name__ == '__main__':
    arm = Arms()
    arm.leftHand(0)
    time.sleep(1)
    arm.leftHand(90)
    time.sleep(1)
    arm.leftHand(180)


    #servo = Translator()
    #servo.balance()

#    mpu = MpuData()
#    mpu.turnOn(0x68)
#    while True:
#        mpu.printValues('b')
#        time.sleep(0.5)

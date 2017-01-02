from drivers.mpu6050.mpudata import MpuData
from drivers.servos.servoTests import servoTest
import time


if __name__ == '__main__':
    servo = servoTest()
    servo.balance()

#    mpu = MpuData()
#    mpu.turnOn(0x68)
#    while True:
#        mpu.printValues('b')
#        time.sleep(0.5)

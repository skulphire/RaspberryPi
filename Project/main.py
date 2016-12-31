import sys
from Project.Drivers.MPU6050 import mpudata

if __name__ == '__main__':
    mpu = mpudata.MpuData()
    mpu.turnOn(0x68)
    while True:
        mpu.getAccXYZ()
        mpu.getGyroXYZ()
        mpu.printValues('a')

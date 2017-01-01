from drivers.mpu6050.mpudata import MpuData
import time


if __name__ == '__main__':
    mpu = MpuData()
    mpu.turnOn(0x68)
    while True:
        mpu.getAccXYZ()
        mpu.getGyroXYZ()
        mpu.printValues('b')
        time.sleep(0.5)

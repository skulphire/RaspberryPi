from Project.Drivers.MPU6050.mpudata import MpuData

if __name__ == '__main__':
    mpu = MpuData()
    mpu.turnOn(0x68)
    while True:
        mpu.getAccXYZ()
        mpu.getGyroXYZ()
        mpu.printValues('a')

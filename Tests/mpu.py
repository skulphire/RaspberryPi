from Tests import mpu6050

class MpuData(object):
    def turnOn(self,address):
        mpu6050.MPU6050.mpuconfig(address)

    def getGyroXYZ(self):
        mpu6050.MPU6050.read_word_2c(0x43)


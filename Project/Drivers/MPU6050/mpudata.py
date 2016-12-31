from Project.Devices.MPU6050 import mpu6050


class MpuData(object):
    def __init__(self):
        self.mpu = mpu6050.MPU6050()
        self.gyroX = 0
        self.gyroY = 0
        self.gyroZ = 0
        self.accX = 0
        self.accY = 0
        self.accZ = 0

    def turnOn(self,address):
        self.mpu.mpuconfig(address)


    #gyro
    def getGyroXYZ(self):
        #getting raw values
        x = self.mpu.read_word_2c(0x43)
        y = self.mpu.read_word_2c(0x45)
        z = self.mpu.read_word_2c(0x47)

        #Scaled values
        self.gyroX=x/131
        self.gyroY=y/131
        self.gyroZ=z/131

    #acc
    def getAccXYZ(self):
        #raw values
        x = self.mpu.read_word_2c(0x3b)
        y = self.mpu.read_word_2c(0x3d)
        z = self.mpu.read_word_2c(0x3f)

        #scaled values
        self.accX = x/16384.0
        self.accY = y/16384.0
        self.accZ = z/16384.0

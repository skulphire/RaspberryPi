from devices.mpu6050.mpu6050 import MPU6050


class MpuData(object):
    def __init__(self):
        self.mpu = MPU6050()
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

    #x rotation from acc
    def getXRotate(self):
        self.getAccXYZ()
        return self.mpu.get_x_rotation(self.accX,self.accY,self.accZ)

    #y rotation from acc
    def getYRotate(self):
        self.getAccXYZ()
        return self.mpu.get_y_rotation(self.accX,self.accY,self.accZ)

    #prints values
    def printValues(self, choice):
        if choice == 'a':
            print("Acc XYZ: ",self.accX," | ",self.accY," | ",self.accZ)
            print("Gyro XYZ: ",self.gyroX," | ",self.gyroY," | ",self.gyroZ)
            print("X rotate: ",self.getXRotate())
            print("Y rotate: ",self.getYRotate())
        elif choice == 'b':
            print("X rotate: ", self.getXRotate())
            print("Y rotate: ", self.getYRotate())
        elif choice == 'c':
            print("Acc XYZ: ", self.accX, " | ", self.accY, " | ", self.accZ)
        elif choice == 'd':
            print("Gyro XYZ: ", self.gyroX, " | ", self.gyroY, " | ", self.gyroZ)
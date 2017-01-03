import time
from drivers.sets.positions import Pos
from drivers.mpu6050.mpudata import MpuData


#usefull commands
#i2cdetect -y 1

if __name__ == '__main__':
    mpu = MpuData()
    position = Pos()
    position.initial()
    while True:
        mpu.printValues('b')
        time.sleep(1)


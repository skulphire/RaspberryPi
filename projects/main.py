import time
from drivers.sets.positions import Pos
from drivers.mpu6050.mpudata import MpuData


#usefull commands
#i2cdetect -y 1

if __name__ == '__main__':
    mpu = MpuData()
    x=0
    y=0
    for i in range(1,5):
        x=mpu.getXRotate()
        y=mpu.getYRotate()
    position = Pos()
    position.initial()
    time.sleep(1)
    position.stop()
    while True:
        x = mpu.getXRotate()
        y = mpu.getYRotate()
        if y > 10:
            position.fallingBack()
        else:
            position.initial()
            position.stop()

    #while True:
        #mpu.printValues('b')
        #time.sleep(1)


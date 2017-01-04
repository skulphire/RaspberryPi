import time
from drivers.sets.positions import Pos
from drivers.mpu6050.mpudata import MpuData


#usefull commands
#i2cdetect -y 1

if __name__ == '__main__':
   position = Pos()
   position.lookRight()
   position.lookLeft()


    #while True:
        #mpu.printValues('b')
        #time.sleep(1)


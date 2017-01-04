import time
from drivers.sets.positions import Pos
from drivers.mpu6050.mpudata import MpuData


#usefull commands
#i2cdetect -y 1

if __name__ == '__main__':
   position = Pos()
   position.lookRight()
   time.sleep(1)
   position.lookLeft()
   time.sleep(2)
   position.stop()


    #while True:
        #mpu.printValues('b')
        #time.sleep(1)


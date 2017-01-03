import time
from drivers.sets.positions import Pos
from drivers.mpu6050.mpudata import MpuData


#usefull commands
#i2cdetect -y 1

if __name__ == '__main__':
   position = Pos()
   position.lookLeft()
   time.sleep(1)
   position.lookRight()
   #position.initial()
   time.sleep(1)

   position.stop()


    #while True:
        #mpu.printValues('b')
        #time.sleep(1)


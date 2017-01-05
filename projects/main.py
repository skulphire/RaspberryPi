import time
from drivers.sets.positions import Pos
from devices.humanoid.arms import Arms
from drivers.mpu6050.mpudata import MpuData


#usefull commands
#i2cdetect -y 1

if __name__ == '__main__':
   position = Pos()
   arm = Arms()
   #position.initial()
   for x in range(0,9):
      position.new()
   time.sleep(3)
   position.stop()


    #while True:
        #mpu.printValues('b')
        #time.sleep(1)


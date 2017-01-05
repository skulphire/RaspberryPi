import time
from drivers.sets.positions import Pos
from devices.humanoid.arms import Arms
from drivers.mpu6050.mpudata import MpuData


#usefull commands
#i2cdetect -y 1

if __name__ == '__main__':
   position = Pos()
   arm = Arms()
   #position.new()
   arm.testerRightShoulder(60,4)
   arm.testerRightShoulder(35, 4)
   time.sleep(5)
   position.stop()


    #while True:
        #mpu.printValues('b')
        #time.sleep(1)


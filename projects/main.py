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

   arm.testerRightShoulder(180,5)
   arm.testerRightShoulder(75, 5)
   arm.testerRightShoulder(150, 5)
   arm.testerRightShoulder(0, 5)

   time.sleep(5)
   position.stop()


    #while True:
        #mpu.printValues('b')
        #time.sleep(1)


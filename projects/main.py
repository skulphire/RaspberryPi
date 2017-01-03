import time
from drivers.sets.positions import Pos
from devices.humanoid.body import Body
from drivers.mpu6050.mpudata import MpuData


#usefull commands
#i2cdetect -y 1

if __name__ == '__main__':
   body = Body()
   position = Pos()
   body.waist(90)
   time.sleep(1)
   body.waist(0)
   time.sleep(1)
   body.waist(45)

   position.stop()


    #while True:
        #mpu.printValues('b')
        #time.sleep(1)


import time

from devices.humanoid.arms import Arms
from drivers.servos.positions import Pos

#usefull commands
#i2cdetect -y 1

if __name__ == '__main__':
   position = Pos()
   arm = Arms()
   #position.initial()
   time.sleep(3)
   position.stop()


    #while True:
        #mpu.printValues('b')
        #time.sleep(1)


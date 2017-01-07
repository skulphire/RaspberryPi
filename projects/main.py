import time

from devices.humanoid.arms import Arms
from drivers.servos.positions import Pos

#usefull commands
#i2cdetect -y 1

if __name__ == '__main__':
   position = Pos()
   arm = Arms()
   arm.leftShoulder(0,5)
   arm.leftElbow(0,5)
   arm.leftHand(180, 5)
   arm.commit()
   #arm.rightShoulder(180,5)
   #arm.rightElbow(180,5)
   #arm.rightHand(0, 5)


   #position.initial()
   time.sleep(3)
   position.stop()


    #while True:
        #mpu.printValues('b')
        #time.sleep(1)


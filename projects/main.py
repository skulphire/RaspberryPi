import time

from devices.humanoid.arms import Arms
from drivers.servos.positions import Pos

#usefull commands
#i2cdetect -y 1

if __name__ == '__main__':
   position = Pos()
   arm = Arms()
   arm.leftShoulder(120,5)
   arm.leftElbow(135,5)
   arm.leftHand(90, 5)
   arm.commit()
   time.sleep(.5)
   arm.leftShoulder(60, 5)
   arm.leftElbow(45, 5)
   arm.leftHand(0, 5)
   arm.commit()
   time.sleep(.5)
   arm.leftShoulder(90, 5)
   arm.leftElbow(180, 5)
   arm.leftHand(90, 5)
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


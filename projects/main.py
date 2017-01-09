import time

from devices.humanoid.arms import Arms
from drivers.servos.positions import Pos

#usefull commands
#i2cdetect -y 1

if __name__ == '__main__':
    position = Pos()
    arm = Arms()

    try:
        position.new()
    except KeyboardInterrupt:
        position.stop()

    #while True:
        #mpu.printValues('b')
        #time.sleep(1)


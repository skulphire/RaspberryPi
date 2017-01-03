import time
from drivers.sets.positions import Pos
#usefull commands
#i2cdetect -y 1

if __name__ == '__main__':
    position = Pos()
    position.start()

    #servo = Translator()
    #servo.balance()

#    mpu = MpuData()
#    mpu.turnOn(0x68)
#    while True:
#        mpu.printValues('b')
#        time.sleep(0.5)

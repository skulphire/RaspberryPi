import smbus
import math
import time

class MPU6050(object):
    #May not need this
    #def __init__(self):

    # Power management registers
    power_mgmt_1 = 0x6b
    power_mgmt_2 = 0x6c

    def read_byte(self, adr):
        return self.bus.read_byte_data(self.address, adr)

    def read_word(self, adr):
        high = self.bus.read_byte_data(self.address, adr)
        low = self.bus.read_byte_data(self.address, adr + 1)
        val = (high << 8) + low
        return val

    def read_word_2c(self, adr):
        val = self.read_word(adr)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val

    def dist(self, a, b):
        return math.sqrt((a * a) + (b * b))

    def get_y_rotation(self, x, y, z):
        radians = math.atan2(x, self.dist(y, z))
        return -math.degrees(radians)

    def get_x_rotation(self, x, y, z):
        radians = math.atan2(y, self.dist(x, z))
        return math.degrees(radians)

    def mpuconfig(self, i2cAdd):
        self.bus = smbus.SMBus(1)  # or bus = smbus.SMBus(1) for Revision 2 boards
        self.address = i2cAdd  # This is the address value read via the i2cdetect command
        # Now wake the 6050 up as it starts in sleep mode
        self.bus.write_byte_data(self.address, self.power_mgmt_1, 0)
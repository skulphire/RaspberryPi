from __future__ import division
import time
from drivers.servos.config import *

class Legs(object):
    def __init__(self):
        self.pulsesDict = TOPPULSESDICT
        self.rankleY = 0 #5
        self.rankleX = 0 #4
        self.rknee = 0 #3
        self.lankleY = 0 #2
        self.lankleX = 0 #1
        self.lknee = 0 #0
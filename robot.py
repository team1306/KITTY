from mecanum import Mecanum
from serial import Serial
from os import listdir
from os.path import isfile

class Robot:
    def __init__(self, a, b, velocityRange=100**3, omegaRange=10**3, usbPort="/dev/ttyUSB0", baud=9600, modulePath="./modules"):
        self.arduino = Serial(usbPort, baud)
        self.driveBase = Mecanum(a, b, velocityRange, omegaRange)
        self.modules = []
        for f in listdir(modulePath):
            if isfile(f):
                self.modules.append(f.rstrip(".py"))

from mecanum import Mecanum
from serial import Serial
from os import listdir
from os.path import isfile, join
from modules import *
from math import sin, cos

class Robot:
    def __init__(self, a, b, velocityRange=100**3, omegaRange=10**3, usbPort="/dev/ttyUSB0", baud=9600, modulePath="./modules", module=None, chip="mega2560", test=False):
        self.driveBase = Mecanum(a, b, velocityRange, omegaRange)
        self.modules = getModules()
        if module is not None and module in self.modules:
            self.module = getInstance(module, usbPort, chip) # self.module is now the object that we need to use
        else: 
            self.module = None
        if not test: # so that this doesn't throw an error when I'm developing
            self.arduino = Serial(usbPort, baud)
        
    def update(self, arguments): # this method will take the entire string sent by the webpage (might be a double)
        args = arguments.split(";")
        args.pop(-1)
        while len(args) > 0: # handles doubles
            data = args[0].split(',')
            self.theta = data[0] # drive processing is built-in
            self.r = data[1]
            self.bytes = self.driveBase.getBytes(self.r*cos(self.theta), self.r*sin(self.theta))
            if self.module is not None:
                self.bytes.append([f for f in self.module.getBytes(data)]) # send all the data to the module expecting list of bytes back
            for b in self.bytes:
                self.arduino.write(b)
                while not self.arduino.inWaiting():
                    pass
                

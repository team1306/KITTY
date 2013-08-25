from mecanum import Mecanum
from serial import Serial
from os import listdir
from os.path import isfile, join
from modules import *
from math import sin, cos

class Robot:
    def __init__(self, a, b, velocityRange=100, omegaRange=0, usbPort="/dev/ttyACM0", baud=9600, modulePath="./modules", module=None, chip="mega2560", test=False):
        print "Loading mecanum drive base"
        self.driveBase = Mecanum(a, b, velocityRange, omegaRange)
        print "Loaded drive base"
        print "Loading module"
        self.modules = getModules()
        self.module = getInstance(module, usbPort, chip) # self.module is now the object that we need to use (None if the module doesn't exist)
        print "Loaded module"
        if not test: # so that this doesn't throw an error when I'm developing
            print "Connecting to Arduino"
            self.arduino = Serial(usbPort, baud)
            print "Successfully connected to Arduino"
            print "Listening for yodel"
            while self.arduino.inWaiting() == 0:
                pass
            print "Heard yodel"
        
    def update(self, arguments): # this method will take the entire string sent by the webpage (might be a double)
        args = arguments.split(";")
        args.pop(-1)
        while len(args) > 0: # handles double messages from socket handler
            data = args.pop().split(',')
            self.theta = float(data[0]) # drive processing is built-in
            self.r = float(data[1])
            print self.r*cos(self.theta)
            print self.r*sin(self.theta)
            self.bytes = self.driveBase.getBytes(self.r*cos(self.theta), self.r*sin(self.theta), 0)
            if self.module is not None:
                self.bytes.append(f for f in self.module.getBytes(data)) # send all the data to the module expecting list of bytes back
            print self.bytes
            for b in self.bytes:
                self.arduino.write(b)
                while not self.arduino.inWaiting():
                    pass
                

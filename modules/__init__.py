from . import *
from subprocess import call
from os import chdir
from os.path import join

# as we write more modules, we need only add an elif to handle the setup of the object
def getInstance(module, usbPort, chip):
    chdir(join("./arduino/", module))
    call(["ino", "build", "-m", chip])
    call(["ino", "upload", "-m", chip, "-p", usbPort])
    if module == "arm":
        mod = arm.Arm()
    elif module == "shooter":
        mod = shooter.Shooter()
    return mod

# this list also needs to be updated as we add more modules so that robot.py doesn't have to look for the modules
def getModules():
    return ["arm", "shooter"]

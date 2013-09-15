from . import *
from subprocess import call
from os import chdir, getcwd
from os.path import join

def flashArduino(module, usbPort, chip):
    if module is not None:
        chdir(join("./arduino/", module)) # current working directory is KITTY
    else:
        chdir("./arduino/base")
    call(["ino", "build", "-m", chip]) # build arduino module in case it's changed
    call(["ino", "upload", "-m", chip, "-p", usbPort]) # flash module onto arduino
    # might want to make that last line only execute if the requested module is different from the last one so as to not flash every time


# as we write more modules, we need only add an elif to handle the setup of the object
# this function turns a string into a module object
# clever, huh?
def getInstance(module, usbPort, chip):
    flashArduino(module, usbPort, chip)
    if module == "arm":
        mod = arm.Arm()
    elif module == "shooter":
        mod = shooter.Shooter()
    else:
        mod = None
    return mod

# this list also needs to be updated as we add more modules so that robot.py doesn't have to look for the modules
def getModules():
    return ["arm", "shooter"]

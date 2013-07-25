from . import *

# as we write more modules, we need only add an elif to handle the setup of the object
def getInstance(module):
    if module == "arm":
        mod = arm.Arm()
    elif module == "shooter":
        mod = shooter.Shooter()
    return mod

# this list also needs to be updated as we add more modules so that robot.py doesn't have to look for the modules
def getModules():
    return ["arm", "shooter"]

import serial
import time

a = serial.Serial("/dev/ttyUSB0", 9600)
time.sleep(1)
print a.inWaiting()
print a.read()
a.close()

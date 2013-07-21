import serial
import time

a = serial.Serial("/dev/ttyUSB0", 115200)
while 1:
    if a.inWaiting() > 0:
        if a.readline().rstrip('\n') == "yodel":
            break
while 1:
    while a.inWaiting() > 0:
        print a.readline()
    a.write(chr(200))

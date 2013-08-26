import serial
import time

a = serial.Serial("/dev/ttyACM0", 9600)
s = a.readline()
print s
while 1:
    time.sleep(1)
    a.write('____')
    time.sleep(1)
    a.write(chr(128)+chr(128)+chr(128)+chr(128))
a.close()

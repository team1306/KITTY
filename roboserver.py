import time
import socket
import threading
import serial
import math
from mecanum import Mecanum
from robot import Robot

if __name__ == "__main__":
    try:
        a = serial.Serial("/dev/ttyUSB0", 115200)
        v = 0
        while a.inWaiting() == 0: # wait for Arduino to send "yodel" so that we know it's ready to start listening
            pass
        print "Initialized Arduino"
        host = ''
        port = 50007
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port)) # open socket on port 50007 to listen for data_wsh.py's messages
        print "Opened socket"
        while 1:
            s.listen(1) # wait for connection
            conn, addr = s.accept() # accept connection
            conn.settimeout(1) # set the timeout to one second so that it takes effect on the subsequent listening
            print 'Connected by', addr
            last = time.time()
            try:
                data = conn.recv(1024) # recieve module name
            except (socket.error, socket.timeout):
                print "\nFailed to recieve module name.\n"
                continue
            robot = Robot(10, 10, module=data)
            while 1:
                try:
                    data = conn.recv(1024) # recieve data
                except (socket.error, socket.timeout): # if data doesn't come soon enough, shut off all motors and terminate the script
                    robot.safeMode()
                    print "\nLost connection with control station.\n"
                    break
                if time.time() - last > 0.5: # same as the try/except (i don't know if this is necessary)
                    last = time.time()
                    break
                last = time.time()
                robot.update(data)
                conn.send("good")
        
    except (KeyboardInterrupt, SystemExit): # if Ctl-C is recieved, exit quietly
        print "\nRecieved keyboard interrupt, quitting server\n"

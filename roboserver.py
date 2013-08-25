import time
import socket
import threading
import serial
import math
import select
from mecanum import Mecanum
from robot import Robot

if __name__ == "__main__":
    try:
        v = 0
        host = ''
        port = 50007
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port)) # open socket on port 50007 to listen for data_wsh.py's messages
        while 1:
            print "Opened socket"
            s.listen(1) # wait for connection
            conn, addr = s.accept() # accept connection
            print 'Connected by', addr
            last = time.time()
            try:
                data = conn.recv(1024) # recieve module name
            except (socket.error, socket.timeout):
                print "\nFailed to recieve module name.\n"
                continue
            print "Initializing Robot"
            robot = Robot(10, 10, module=data.lstrip("mod:"), chip="atmega328")
            print "Successfully initialized Robot"
            while 1:
                try:
                    data = conn.recv(1024) # recieve data
                except (socket.error, socket.timeout): # if data doesn't come soon enough, shut off all motors and terminate the script
                    robot.safeMode()
                    print "\nLost connection with control station.\n"
                    break
                #if time.time() - last > 0.5: # same as the try/except (i don't know if this is necessary)
                    #last = time.time()
                    #break
                last = time.time()
                robot.update(data) # lets the robot update itself
                conn.send("good")
        
    except (KeyboardInterrupt, SystemExit): # if Ctl-C is recieved, exit quietly
        print "\nRecieved keyboard interrupt, quitting server\n"

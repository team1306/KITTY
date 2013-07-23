import time
import socket
import threading
import serial
import math

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
            while 1:
                try:
                    data = conn.recv(1024) # recieve data
                except (socket.error, socket.timeout): # if data doesn't come soon enough, shut off all motors and terminate the script
                    tr = (0, 0)
                    print "\nLost connection with control station.\n"
                    break
                if time.time() - last > 0.5: # same as the try/except (i don't know if this is necessary)
                    last = time.time()
                    break
                last = time.time()
                if data.count(",") > 5 or data.count(",") == 0: # sometimes there are two lines of data waiting in the queue, so for now it just ignores messages that are abnormally long
                    continue
                theta = float(data.split(",")[0]) # extract data that governs the motor speed
                r = float(data.split(",")[1])
                q = r*math.sin(theta) + 100 
                if q > 0 and q < 200: # send the motor speed
                    a.write(chr(int(round(q))))
                    v = q
                elif q > 200: # set motor speed to the limits if the input value is outside of the limits
                    a.write(chr(200))
                    v = 200
                elif q < 0:
                    a.write(chr(0))
                    v = 0
                print 83*v/10 + 670
                conn.send("good")
        
    except (KeyboardInterrupt, SystemExit): # if Ctl-C is recieved, exit quietly
        print "\nRecieved keyboard interrupt, quitting server\n"

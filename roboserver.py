import time
import socket
import threading
import serial
import math

if __name__ == "__main__":
    try:
        a = serial.Serial("/dev/ttyUSB0", 115200)
        v = 0
        while a.inWaiting() == 0:
            pass
        print "Initialized Arduino"
        host = ''
        port = 50007
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        print "Opened socket"
        while 1:
            s.listen(1)
            conn, addr = s.accept()
            conn.settimeout(1)
            print 'Connected by', addr
            last = time.time()
            while 1:
                try:
                    data = conn.recv(1024)
                except (socket.error, socket.timeout):
                    tr = (0, 0)
                    print "\nLost connection with control station.\n"
                    break
                if time.time() - last > 0.5:
                    last = time.time()
                    break
                last = time.time()
                if data.count(",") > 1 or data.count(",") == 0:
                    continue
                theta = float(data.split(",")[0])
                r = float(data.split(",")[1])
                q = r*math.sin(theta) + 100
                if q > 0 and q < 200:
                    a.write(chr(int(round(q))))
                    v = q
                elif q > 200:
                    a.write(chr(200))
                    v = 200
                elif q < 0:
                    a.write(chr(0))
                    v = 0
                print 83*v/10 + 670
                conn.send("good")
        
    except (KeyboardInterrupt, SystemExit):
        print "\nRecieved keyboard interrupt, quitting server\n"

from math import sin, cos

class Mecanum:
    def __init__(self, a, b, velocityRange=50, omegaRange=0): 
        # the ranges are centered at 0, so the actual range of acceptable velocity values is [-velocityRange, velocityRange]
        # the range is also the range for v_x and v_y, not |v|
        self.a = a
        self.b = b
        self.maxVelocity = velocityRange
        self.minVelocity = -velocityRange
        self.maxOmega = omegaRange
        self.minOmega = -omegaRange

    # wheel numbers are assigned as follows from a top view
    # 1: front right
    # 2: front left
    # 3: back left
    # 4: back right

    def getVelocities(self, vx, vy, omega): # returns ideal velocities of each wheel
        vw1 = vy - vx + omega*(self.a + self.b)
        vw2 = vy + vx - omega*(self.a + self.b)
        vw3 = vy - vx - omega*(self.a + self.b)
        vw4 = vy + vx + omega*(self.a + self.b)
        return (vw1, vw2, vw3, vw4)

    def scaleVelocities(self, velocities): # scales all of the speeds so that none of them exceed the maximum motor speed
        scaled = []
        for v in velocities:
            scaled.append(float(v*255/(2*(self.maxVelocity + self.maxVelocity + self.maxOmega*(self.a + self.b)))) + 127.5)
        return scaled

    def getBytes(self, vx, vy, omega): # returns the bytes to control the Arduino
        velocities = self.scaleVelocities(self.getVelocities(vx, vy, omega))
        b = []
        for v in velocities:
            b.append(chr(int(round(v))))
        return b

import gpiozero # learn more: https://python.org/pypi/gpiozero
import time

from IC74HC595 import *

FORWARD = 1
BACKWARD = -1

def dutyCycle(speed):
    return 0.2 + 0.8*speed

class L293DMDS:
    def __init__(self, pwmMA, pwmMB, pwmMC, pwmMD, pwmServo1, pwmServo2, dataPin, clockPin, latchPin):
        self.motorControl = IC74HC595(dataPin, clockPin, latchPin)
        self.pwmMA = gpiozero.PWMOutputDevice(pwmMA)
        self.pwmMB = gpiozero.PWMOutputDevice(pwmMB)
        self.pwmMC = gpiozero.PWMOutputDevice(pwmMC)
        self.pwmMD = gpiozero.PWMOutputDevice(pwmMD)
        self.pwmServo1 = gpiozero.PWMOutputDevice(pwmServo1)
        self.pwmServo2 = gpiozero.PWMOutputDevice(pwmServo2)

    def stop(self):
        self.motorControl.write([0, 0, 0, 0, 0, 0, 0, 0])
        self.pwmMA.off()
        self.pwmMB.off()
        self.pwmMC.off()
        self.pwmMD.off()
        
    def run(self, leftDir=FORWARD, rightDir=FORWARD, leftSpeed=1.0, rightSpeed=1.0):
        if leftDir == FORWARD:
            if rightDir == FORWARD:
               self.motorControl.write([0, 0, 1, 0, 0, 1, 1, 1])
            else:
               self.motorControl.write([1, 0, 0, 1, 0, 1, 0, 1])
        else:
            if rightDir == FORWARD:
                self.motorControl.write([0, 1, 1, 0, 1, 0, 1, 0])
            else:
                self.motorControl.write([1, 1, 0, 1, 1, 0, 0, 0])

        self.pwmMA.value = self.pwmMC.value = dutyCycle(leftSpeed)
        self.pwmMB.value = self.pwmMD.value = dutyCycle(rightSpeed)
        
    def motorARun(self, direction=FORWARD, speed=1.0):
        if direction == FORWARD:
            self.motorControl.write([0, 0, 0, 0, 0, 0, 0, 1])
        else:
            self.motorControl.write([0, 1, 0, 0, 0, 0, 0, 0])
        self.pwmMA.value = dutyCycle(speed)

    def motorBRun(self, direction=FORWARD, speed=1.0):
        if direction == FORWARD:
            self.motorControl.write([0, 0, 1, 0, 0, 0, 0, 0])
        else:
            self.motorControl.write([1, 0, 0, 0, 0, 0, 0, 0])
        self.pwmMB.value = dutyCycle(speed)

    def motorCRun(self, direction=FORWARD, speed=1.0):
        if direction == FORWARD:
            self.motorControl.write([0, 0, 0, 0, 0, 1, 0, 0])
        else:
            self.motorControl.write([0, 0, 0, 0, 1, 0, 0, 0])
        self.pwmMC.value = dutyCycle(speed)

    def motorDRun(self, direction=FORWARD, speed=1.0):
        if direction == FORWARD:
            self.motorControl.write([0, 0, 0, 0, 0, 0, 1, 0])
        else:
            self.motorControl.write([0, 0, 0, 1, 0, 0, 0, 0])
        self.pwmMD.value = dutyCycle(speed)

if __name__ == "__main__":

    try:
        mdr = L293DMDS(16, 12, 20, 21, 19, 26, 24, 25, 23)
        while True:
            mdr.run(leftDir=FORWARD, rightDir=BACKWARD) 
            time.sleep(5)
    except:
	mdr.stop()

    mdr.stop()
     

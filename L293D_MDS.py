import gpiozero # learn more: https://python.org/pypi/gpiozero

from IC74HC595 import *

class L293DMDS:
    def __init__(self, pwmM1, pwmM2, pwmM3, pwmM4, pwmServo1, pwmServo2, dataPin, clockPin, latchPin):
        self.motorControl = IC74HC595(dataPin, clockPin, latchPin)
        self.pwmM1 = gpiozero.PWMOutputDevice(pwmM1)
        self.pwmM2 = gpiozero.PWMOutputDevice(pwmM2)
        self.pwmM3 = gpiozero.PWMOutputDevice(pwmM3)
        self.pwmM4 = gpiozero.PWMOutputDevice(pwmM4)
        self.pwmServo1 = gpiozero.PWMOutputDevice(pwmServo1)
        self.pwmServo2 = gpiozero.PWMOutputDevice(pwmServo2)

    def allStop():
        self.motorControl.write([0, 0, 0, 0, 0, 0, 0, 0])
        
    def allForward():
        self.motorControl.write([1, 1, 1, 0, 0, 1, 0, 0])
        
    def allBackward():
        self.motorControl.write([0, 0, 0, 1, 1, 0, 1, 1])

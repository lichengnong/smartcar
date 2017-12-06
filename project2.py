import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setmode(GPIO.BOARD)     # Numbers GPIOs based on physical location
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.setup(ledPin2, GPIO.OUT)
    GPIO.output(ledPin2, GPIO.LOW)
    GPIO.setup(ledPin3, GPIO.OUT)
    GPIO.output(ledPin3, GPIO.LOW)

ledPin = 11
ledPin2 = 13
ledPin3 = 15

def loop():
    while True:
        GPIO.output(ledPin, GPIO.HIGH)
        print "green light"
        time.sleep(10)
        GPIO.output(ledPin, GPIO.LOW)
        GPIO.output(ledPin2, GPIO.HIGH)
        print "yellow light"
        time.sleep(3)
        GPIO.output(ledPin2, GPIO.LOW)
        GPIO.output(ledPin3, GPIO.HIGH)
        print "red light"
        time.sleep(10)
        GPIO.output(ledPin3, GPIO.LOW)        

def destroy():
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.output(ledPin2, GPIO.LOW)
    GPIO.output(ledPin3, GPIO.LOW)
    GPIO.cleanup()
    
if __name__ == '__main__':
    setup()
    try:
        loop()
        loop2()
        loop3()
    except KeyboardInterrupt:
        destroy()

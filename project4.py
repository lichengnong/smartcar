import RPi.GPIO as GPIO
import time
ledpin = 12
def setup():
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledpin, GPIO.OUT)
    GPIO.output(ledpin, GPIO.LOW)
    p = GPIO.PWM(ledpin, 50)
    p.start(0)
def loop():
    while True:
        for dc in range(0, 100, 1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
        time.sleep(0.5)
        for dc in range(100, 0, -1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
        time.sleep(0.5)
def destroy():
    p.stop()
    GPIO.output(ledpin, GPIO.LOW)
    GPIO.cleanup()
if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

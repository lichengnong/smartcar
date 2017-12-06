import RPi.GPIO as GPIO
import time

pwm_pin = 15
in2_pin = 11
in1_pin = 13

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(in1_pin, GPIO.OUT)
    GPIO.output(in1_pin, GPIO.LOW) 
    GPIO.setup(in2_pin, GPIO.OUT)
    GPIO.output(in2_pin, GPIO.LOW)
    GPIO.setup(pwm_pin, GPIO.OUT)
    GPIO.output(pwm_pin, GPIO.LOW)
    p = GPIO.PWM(pwm_pin, 100)
    p.start(0)

def loop():
    while True:
        GPIO.output(in1_pin, GPIO.HIGH) 
        GPIO.output(in2_pin, GPIO.LOW) 
        for dc in range(30, 101, 10):
            p.ChangeDutyCycle(dc)
            time.sleep(1)
        time.sleep(0.5)
        GPIO.output(in1_pin, GPIO.LOW) 
        GPIO.output(in2_pin, GPIO.HIGH) 
        for dc in range(100, 29, -10):
            p.ChangeDutyCycle(dc)
            time.sleep(1)
        time.sleep(0.5)

def destroy():
    p.stop()
    GPIO.output(pwm_pin, GPIO.LOW)
    GPIO.output(in1_pin, GPIO.LOW)
    GPIO.output(in2_pin, GPIO.LOW)
    GPIO.cleanup()
if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

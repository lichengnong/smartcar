import RPi.GPIO as GPIO

ledpin = 11
buttonpin = 12

def setup():
    print 'Program is starting...'
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledpin, GPIO.OUT)
    GPIO.setup(buttonpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    while True:
        if GPIO.input(buttonpin)==GPIO.LOW:
            GPIO.output(ledpin,GPIO.HIGH)
            print 'LED on...'
        else :     
            GPIO.output(ledpin,GPIO.LOW)
            print 'LED off...'

def destroy():
    GPIO.output(ledpin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

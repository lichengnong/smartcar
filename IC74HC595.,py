import gpiozero # learn more: https://python.org/pypi/gpiozero

class IC74HC595:
    def __init__(self, dataPin, clockPin, latchPin):
        self.dataPin = gpiozero.LED(dataPin)
        self.clockPin = gpiozero.LED(clockPin)
        self.latchPin = gpiozero.LED(latchPin)
    
    def write(self, valueList):
        self.latchPin.off()

        for v in valueList:
            self.clockPin.off()
            
            if v:
                self.dataPin.on()
            else:
                self.dataPin.off()
                
            self.clockPin.on()

        self.dataPin.off()        
        self.clockPin.off()
        
        self.latchPin.on();
        self.latchPin.off();
        

# import RPi.GPIO as GPIO
import setup_gpio

# pins = [PIN_A, PIN_B, PIN_C, PIN_D, PIN_E, PIN_F]
class sl_gpio :

    try:
        #while True :
        def __init__ (self) :
            print("init")
            global pins
            # self.GPIO.setmode(GPIO.BOARD)
            for self.pin in pins:
                print self.pin
                # self.GPIO.setup(self.pi,GPIO.OUT)

        def set (self, pin, val) :
            print("set")

        def update() :
            pass

    except KeyboardInterrupt :
    	GPIO.cleanup()

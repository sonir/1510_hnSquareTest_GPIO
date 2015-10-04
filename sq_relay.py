import RPi.GPIO as GPIO
import sq_osc, time

class SquareRelay :
    def __init__ (self, interval) :
        self.RELAY1=3
        self.RELAY2=5
        self.RELAY3=7
        self.RELAY4=11
        self.PANEL_RELAY1=13
        self.PANEL_RELAY2=15
        self.pins = [self.RELAY1, self.RELAY2, self.RELAY3, self.RELAY4, self.PANEL_RELAY1, self.PANEL_RELAY2]

        self.RELAY_MAX = 6
        self.MAX_PIN = 15
        self.SEQ_SPD = interval
        # self.SEQ_SPD = 0.002
        self.seqs = []
        self.setup()
        self.flg = 0

    def setup (self) :
        self.gpio_setup()
        for var in range(0, self.RELAY_MAX):
            s = sq_osc.SquareOsc(self.SEQ_SPD)
            self.seqs.append( s )

    def gpio_setup (self) :
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.RELAY1,GPIO.OUT)
        GPIO.setup(self.RELAY2,GPIO.OUT)
        GPIO.setup(self.RELAY3,GPIO.OUT)
        GPIO.setup(self.RELAY4,GPIO.OUT)
        GPIO.setup(self.PANEL_RELAY1,GPIO.OUT)
        GPIO.setup(self.PANEL_RELAY2,GPIO.OUT)


    def update (self) :
        self.num = 0

        # SET for count is OK
        assert self.RELAY_MAX==6
        for var in range(0, self.RELAY_MAX):
            self.num=self.num+1
            self.flg = self.seqs[var].cycle()
            if self.flg == 1 :
                print "on"
                GPIO.output(self.pins[var],True)
                time.sleep(0.1)
            elif self.flg == 0 :
                GPIO.output(self.pins[var],False)
                print "off"
            else :
                print "unknown"

        # for is working correctlly.
        assert self.num == 6


    def on (self,relay_num) :
        # GPIO.output(self.pins[relay_num],True)
        # print "SEQ:bang"
        self.seqs[relay_num].bang()

    def off (self,relay_num) :
        pass
        # GPIO.output(self.pins[relay_num],False)

    def terminate(self) :
        GPIO.cleanup()

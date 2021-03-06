# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time, sq_osc

# sqo = sq_osc.SquareOsc(0.002)
sqo = sq_osc.SquareOsc(1)
sqo.bang()
COUNT = 3
PIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN,GPIO.OUT)

try:
	while True :
		flg = sqo.cycle()
		if flg == 1 :
			GPIO.output(PIN,True)
			time.sleep(0.1)
			print("ON")
		elif  flg == 0 :
			GPIO.output(PIN,False)
		elif flg == -2 :
			sqo.bang()
			pass;

except KeyboardInterrupt :
	GPIO.cleanup()

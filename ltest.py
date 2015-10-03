# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

PIN=11
PIN2=13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN,GPIO.OUT)
GPIO.setup(PIN2,GPIO.OUT)

try:
	while True :
		print "ON"
                GPIO.output(11, True)
                GPIO.output(13, False)
		time.sleep(0.2)
		GPIO.output(11, False)
                GPIO.output(13, True)
		print "OFF"
		time.sleep(0.2)

except KeyboardInterrupt :
	GPIO.cleanup()

# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

COUNT = 3
PIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN,GPIO.OUT)

# for _ in xrange(COUNT):
#     GPIO.output(PIN,True)
#    time.sleep(1.0)
#     GPIO.output(PIN,False)
#     time.sleep(1.0)

<<<<<<< HEAD
while True :
	GPIO.output(PIN,True)
	time.sleep(1.0)
	GPIO.output(PIN,False)
	time.sleep(1.0)

#except KeyboardInterrupt:
# print("detect key interrupt\n")
 
#GPIO.cleanup()
#print("Program exit\n")

=======
try:
	while True :
		GPIO.output(PIN,True)
		time.sleep(1.0)
		GPIO.output(PIN,False)
		time.sleep(1.0)

except KeyboardInterrupt :
	GPIO.cleanup()
>>>>>>> f480d7a9b984f648c18f5d013f8fe5b06c2a60c5

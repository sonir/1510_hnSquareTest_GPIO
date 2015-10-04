import sq_receive
print "Square system is started"
osc = sq_receive.SquareReceive(5137)
osc.setup()

try:
    while True:
        print "ff"

except KeyboardInterrupt :
	osc.terminate()

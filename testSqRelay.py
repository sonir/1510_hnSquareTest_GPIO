import sq_relay

try:
    s = sq_relay.SquareRelay(0.002)
    s.setup()
    s.on(0)
    print "---"
    s.update()
    print "---"
    s.update()
    print "---"
    s.update()
    # while True :
    #     s.update()

except KeyboardInterrupt :
	s.terminate()

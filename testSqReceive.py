import sq_receive

try:
    r = sq_receive.SquareReceive(7000)
    r.setup()

    while True:
        r.update()

except KeyboardInterrupt :
	r.terminate()

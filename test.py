import sq_osc


sqo = sq_osc.SquareOsc(0.1)
sqo.bang()

while(1):
    #global metro
    sqo.update()
    # pass#print(1)

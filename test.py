import sq_osc


sqo = sq_osc.SquareOsc(0.015)
sqo.bang()
flg = 0

while(1):
    #global metro
    flg = sqo.update()
    if flg == 1 :
        print("-----------ON")
    if flg == 0 :
        print("OFF")
        pass;
    if flg == -1 :
        # print("rest")
        pass;

    # pass#print(1)

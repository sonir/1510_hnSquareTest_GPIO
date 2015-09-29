import t_metro

metro = t_metro.Metro(1.0)

blinker = False

while(1):
    #global metro
    if metro.update() :
        blinker = ~blinker
        if blinker:
            print("OK")
        else:
            print("NULL")

        # pass#print(1)

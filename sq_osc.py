import sl_metro

class SquareOsc:

    def __init__(self, interval):
        self.metro = sl_metro.Metro( (interval*0.1) )
        self.list = [1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.LIST_MAX = 9
        self.now = 0
        self.rotation = 0
        self.CLICK_TIME = 4
        self.bang_flg = False

    def bang(self) :
        self.bang_flg = True
        self.metro.reset()

    def reset(self):
        self.bang_flg = False
        self.rotation = 0
        self.now = 0

    def countCheck(self):
        if self.rotation < self.CLICK_TIME :
            return True
        else:
            print "Finish ALL."
            self.reset()
            return False

    def endCheck(self):
        if self.now >= self.LIST_MAX :
            print "finish play seq. loop"
            self.now = 0
            self.rotation += 1
            return True
        else:
            return False

    def seqCheck(self):
        if self.list[self.now]==1 :
            print "the seq is ON RT1"
            self.now +=1
            return True
        elif self.list[self.now]==0 :
            print "the seq is OFF RT0"
            self.now +=1
            return False

    def cycle (self) :
        # print "SQOSC UPDATE"
        # return 137

        if self.bang_flg==False :
            return -1

        if self.metro.update() :
            if self.countCheck():
                if self.endCheck()==True:
                    return 0
                else:
                    if self.seqCheck()==True:
                        return 1
                    else:
                        return 0
            else:
                #FINISH
                return -2
        else:
            return -1

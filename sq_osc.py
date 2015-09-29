import sl_metro

class SquareOsc:
    def __init__ (self, interval) :
        self.metro = sl_metro.Metro(interval)
        self.blinker = False
        self.counter = 0
        self.list = [1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.list_max = 9
        self.now = 0
        self.rotation = 0
        self.click_times = 4
        self.bang_flg = False

    def bang(self):
        self.bang_flg = True

    def update (self) :
            if self.metro.update() :
                while(self.rotation < self.click_times):
                    if self.now >= self.list_max :
                        self.now = 0
                        self.rotation += 1
                    elif self.list[self.now]==1:
                        self.now +=1
                        print("OK")
                    else:
                        print("NULL")
                        self.now +=1
                self.bang_flg = False

            return self.bang_flg


                # self.blinker = ~self.blinker
                # if self.blinker:
                #     print("OK")
                # else:
                #     print("NULL")

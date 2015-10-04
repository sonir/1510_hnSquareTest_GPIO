import sl_receive
class SquareReceive(sl_receive.SlReceive):

    def __init__(self,port):
        sl_receive.SlReceive.__init__(self, port)

    def setup(self):
        sl_receive.SlReceive.setup(self)

    def addMsgHandlers(self):
        self.s.addMsgHandler("/test3", self.test3)

    def test3(self, add, tags, stuff, source):
        print "test3"

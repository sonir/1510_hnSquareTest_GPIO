import sl_receive
class SquareReceive(sl_receive.SlReceive):

    def __init__(self,port):
        sl_receive.SlReceive.__init__(self, port)

    def setup(self):
        sl_receive.SlReceive.setup(self)

    def addMsgHandlers(self):
        self.s.addMsgHandler("/trigger", self.trigger)

    def trigger(self, add, tags, stuff, source):
        print ("Trigger")

    # def terminate(self):
    #     print "SQOSC:Terminated."
    #
    # def update(self):
    #     pass

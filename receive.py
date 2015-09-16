import socket, OSC, re, time, threading, math

receive_address = '127.0.0.1', 7000 #Mac Adress, Outgoing Port

class PiException(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)


s = OSC.OSCServer(receive_address)
s.addDefaultHandlers()


def test(add, tags, stuff, source):
	print("test1")

def test2(add, tags, stuff, source):
	print "X Value is: "
	print stuff[0]
	print "Y Value is: "
	print stuff[1]  #stuff is a 'list' variable


def moveStop_handler(add, tags, stuff, source):
	addMove(0,0)

s.addMsgHandler("/test", test)
s.addMsgHandler("/test2", test2)


# just checking which handlers we have added
print "Registered Callback-functions are :"
for addr in s.getOSCAddressSpace():
	print addr


# Start OSCServer
print "\nStarting OSCServer. Use ctrl-C to quit."
st = threading.Thread( target = s.serve_forever )
st.start()


# Loop while threads are running.
try :
	while 1 :
		time.sleep(10)

except KeyboardInterrupt :
	print "\nClosing OSCServer."
	s.close()
	print "Waiting for Server-thread to finish"
	st.join()
	print "Done"

from multiprocessing.connection import Listener
li=[]
address = ('localhost', 6000)     # family is deduced to be 'AF_INET'
listener = Listener(address, authkey='secret password')
conn = listener.accept()
print 'connection accepted from', listener.last_accepted
while True:
    msg = conn.recv()
    li.append(msg)# do something with msg
    if msg == 'close':
			conn.send(li)
			print("sending data in FIFO order...")
        	#conn.close()
			break
print("data sent!")
listener.close()

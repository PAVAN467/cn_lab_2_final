from multiprocessing.connection import Client

address = ('localhost', 6000)
conn = Client(address, authkey='secret password')
conn.send('hello')
conn.send('world')
conn.send('close')
x=conn.recv()
print x
# can also send arbitrary objects:
# conn.send(['a', 2.5, None, int, sum])
conn.close()

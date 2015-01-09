import zmq

cxt = zmq.Context()
print 'Connecting to server...'
socket = cxt.socket(zmq.REQ)
socket.connect("ipc://back_sock")

print 'Sendng...'
socket.send('Hello')
msg = socket.recv()
print msg
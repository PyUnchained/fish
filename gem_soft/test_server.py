import zmq
import time
import uuid
from  multiprocessing import Process

def producer():
    context = zmq.Context()
    send_socket = context.socket(zmq.PUSH)
    send_socket.bind("tcp://127.0.0.1:5000")

    for num in xrange(1000):
        if num % 3 == 0:
            work = {'type':'wrong','msg':'Some Message'}
            send_socket.send_json(work)
        else:
            work = {'type':'msg','msg':'Some Message'}
            send_socket.send_json(work)

def consumer(consumer_id = None):
    #set id and create context
    if consumer_id == None:
        consumer_id = uuid.uuid4()
    context = zmq.Context()
    
    #receive work
    recv_socket = context.socket(zmq.PULL)
    recv_socket.connect("tcp://127.0.0.1:5000")
    
    #send completed work
    send_socket = context.socket(zmq.PUSH)
    send_socket.connect("tcp://127.0.0.1:5001")
    
    while True:
        work = recv_socket.recv_json()
        if work['type'] == 'msg':
            result = {'data':work, 'pass':True, 'consumer':consumer_id}
            send_socket.send_json(result)
        else:
            result = {'data':work, 'pass':False, 'consumer':consumer_id}
            send_socket.send_json(result)

def collector():
    context = zmq.Context()
    recv_socket = context.socket(zmq.PULL)
    recv_socket.bind("tcp://127.0.0.1:5001")
    collector_data = {}

    while True:
        new_data = recv_socket.recv_json()

        #if the consumer's output is already being tracked and the data
        #sent passed through the consumer as expected
        if collector_data.has_key(new_data['consumer']):
            if new_data['pass'] == True:
                collector_data[new_data['consumer']] += 1

        #if not, begin tracking it if the data passed through the consumer
        #as expected
        else:
            if new_data['pass'] == True:
                collector_data[new_data['consumer']] = 1

if __name__ == "__main__":
    #Start collector
    Process(target=collector).start()

    #Start 3 consumers
    for i in range(0,3):
        Process(target=consumer, args = (i,)).start()

    #Start the producer.
    Process(target=producer).start()

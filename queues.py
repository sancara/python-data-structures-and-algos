from . import nodes.Node 

class Queue:
    '''
    Queues are a sequence of nodes.
    It starts with a head, and are unidirectional, they process data first in, first out -> FIFO
    - get_head_node returns where the linked list starts.
    - enqueue add a node to the back of the queue. The first added node is the head and also the tail of the queue.
    - dequeue remove an item from the front, returning the value
    - peek shows the front of the queue without retrieving it
    '''
    
    def __init__(self):
        self.head = None
        self.tail = None
  
    def peek(self):
        return self.head.get_value()


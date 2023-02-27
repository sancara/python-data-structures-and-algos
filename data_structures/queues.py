from mypackage.nodes import Node 

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

    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            print(f'Adding {item_to_add.get_value()} to the queue!')
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.next_node = (item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Sorry, no more room!")
    
    def dequeue(self):
        if not self.is_empty():
            item_to_remove = self.head
            print(f'Removing {item_to_remove.get_value()} from the queue!')
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("This queue is totally empty!")
    
    def peek(self):
        if self.is_empty():
            print("Nothing to see here!")
        else:
            return self.head.get_value()
  
    def get_size(self):
        return self.size
  
    def has_space(self):
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.get_size()
    
    def is_empty(self):
        return self.size == 0


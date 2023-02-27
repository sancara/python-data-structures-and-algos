from . import Node

class Stack:
    '''
    Similiar to queues, but under the premise of
    Last In First Out LIFO

    methods: 
        Push: to add to the top of the stack
        Pop: remove and return the value of the top
        Peek: return the value of the top without removing

    Stacks can have limits uper stack overflow, trying to pop
    an empty stack, stack underflow
    '''
    def __init__(self, limit=1000, name:str=None):
        self.top_item = None
        self.size = 0
        self.limit = limit
        self.name = name
  
    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
    # Increment stack size by 1 here:
            self.size += 1
        else:
            return "All out of space!"

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            return "This stack is totally empty."
  
    def peek(self):
        if not self.is_empty():
	        return self.top_item.get_value()
        else:
            return "Nothing to see here!"
      
  # Define has_space() and is_empty() below:
    def has_space(self):
        return self.limit > self.size
  
    def is_empty(self):
        return self.size == 0
  

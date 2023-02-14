from . import nodes.Node

class LinkedList:

    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):

        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node


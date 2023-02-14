from . import nodes.Node

class LinkedList:
    '''
    Linked Lists are a sequence of nodes.
    It starts with a head, and can be uni o bidirectional,
    - get_head_node returns where the linked list starts.
    - insert_beginning first instanciate a new node and then links it to the current head_node,
    consecuently after setting the new node as head node it becomes the first node in the linked list
    without losing any information.
    - stringify_list shows the values from each node in the linked list
    '''
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):

        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):

        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += f'{current_node.get_value()}
            current_node = current_node.get_next_node()
        return string_list
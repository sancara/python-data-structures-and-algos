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
    - remove_node remove a node by it's value
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
    
    def remove_node(self, value_to_remove):
        current_node = self.head_node
    
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()  
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

'''
Swapping elements in a linked list
'''

def swap_nodes(input_list, val1, val2):
  print(f'Swapping {val1} with {val2}')

  node1_prev = None
  node2_prev = None
  node1 = input_list.head_node
  node2 = input_list.head_node

  if val1 == val2:
    print("Elements are the same - no swap needed")
    return

  while node1 is not None:
    if node1.get_value() == val1:
      break
    node1_prev = node1
    node1 = node1.get_next_node()

  while node2 is not None:
    if node2.get_value() == val2:
      break
    node2_prev = node2
    node2 = node2.get_next_node()

  if (node1 is None or node2 is None):
    print("Swap not possible - one or more element is not in the list")
    return

  if node1_prev is None:
    input_list.head_node = node2
  else:
    node1_prev.set_next_node(node2)

  if node2_prev is None:
    input_list.head_node = node1
  else:
    node2_prev.set_next_node(node1)

  temp = node1.get_next_node()
  node1.set_next_node(node2.get_next_node())
  node2.set_next_node(temp)


ll = LinkedList.LinkedList()
for i in range(10):
  ll.insert_beginning(i)

print(ll.stringify_list())
swap_nodes(ll, 9, 5)
print(ll.stringify_list())
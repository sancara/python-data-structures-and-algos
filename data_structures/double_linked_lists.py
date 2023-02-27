from . import Node
    
class DoublyLinkedList:
  '''
    Double Linked Lists are a sequence of nodes.
    It starts with a head, they are bidirectional,
    - get_head_node returns where the linked list starts.
    - add_to_head: consecuently after setting the new node as head node, 
    it becomes the first node in the double linked list,
    without losing any information.
    - add_to_tail: consecuently after setting new node as tail node,
    it becomes the last node in the double linked list,
    without losing any information.
    - remove_head: change the pointer from the current head to next node,
    remove the current head node, making the next one the new head.
    - remove_tail: change the pointer from the current tail to prev node,
    remove the current tail node, making the prev node the new tail.
    - remove_by_value: method needed when the node to remove is not the head,
    neither the tail, you pass a value, then this method iterate the list,
    when matched, change the pointers (next and prev), making the value orphan.
    - stringify_list shows the values from each node in the linked list
    '''
  def __init__(self):
    self.head_node = None
    self.tail_node = None

  def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += f'{current_node.get_value()}'
            current_node = current_node.get_next_node()
        return string_list
  
  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node

    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)

    self.head_node = new_head

    if self.tail_node == None:
      self.tail_node = new_head

  def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node

    if current_tail != None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)

    self.tail_node = new_tail

    if self.head_node == None:
      self.head_node = new_tail

  def remove_head(self):
    removed_head = self.head_node

    if removed_head == None:
      return None

    self.head_node = removed_head.get_next_node()

    if self.head_node != None:
      self.head_node.set_prev_node(None)

    if removed_head == self.tail_node:
      self.remove_tail()

    return removed_head.get_value()

  def remove_tail(self):
    removed_tail = self.tail_node

    if removed_tail == None:
      return None

    self.tail_node = removed_tail.get_prev_node()

    if self.tail_node != None:
      self.tail_node.set_next_node(None)

    if removed_tail == self.head_node:
      self.remove_head()

    return removed_tail.get_value()

  def remove_by_value(self, value_to_remove):
    node_to_remove = None
    current_node = self.head_node

    while current_node != None:
      if current_node.get_value() == value_to_remove:
        node_to_remove = current_node
        break

      current_node = current_node.get_next_node()

    if node_to_remove == None:
      return None
    
    if node_to_remove == self.head_node:
      self.remove_head()
    elif node_to_remove == self.tail_node:
      self.remove_tail()
    else:
      next_node = node_to_remove.get_next_node()
      prev_node = node_to_remove.get_prev_node()
      next_node.set_prev_node(prev_node)
      prev_node.set_next_node(next_node)
    
    return node_to_remove



class Node:
 '''
 This is Node.
    when instanciating it's need to pass a value which will be the data.
    the next_node by default is None, so it's no needed.
    by the methods you can retrieve the value but data remains inmutable.
    set_next_node is used to change the node pointer

    if there's a link to other nodes you can retrieve the following node data using:
        node.get_next_node().get_value()
 '''
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def get_prev_node(self):
    return.self.prev_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
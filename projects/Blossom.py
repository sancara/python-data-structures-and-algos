from ..data_structures.linked_lists import LinkedList
from ..data_structures.nodes import Node

class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for e in range(self.array_size)]
        
    def hash(self, key):
        hash_code = sum(key.encode()) 
        return hash_code
    
    def compress(self, hash_code):
        return hash_code % self.array_size
    
    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        payload = Node([key, value])
        list_at_array = self.array[array_index]
        for i in list_at_array:
            if i[0] == key:
                i[1] = value
        list_at_array.insert(payload)

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index  = self.array[array_index]
        for e in list_at_index:
            if e[0] == key:
                return e[1]
            else:
                return None
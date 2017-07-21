#Implement of doubly linked list
class DoublyListNode(object):
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
    
class DoublyList(object):
  def __init__(self):
    self.head = DoublyListNode(None)
    self.tail = DoublyListNode(None)
    self.head.next = self.tail
    self.tail.prev = self.head
    self.count = 0
    
  def __len__(self):
    return self.count
    
  def __index__(self, data):
    index = -1
    cur = self.head
    
    while cur:
      if cur.data == data:
        return index
      index += 1
      cur = cur.next
      
    return index
    
  def isEmpty():  
    return self.count == 0
  
  def add_node_at_head(self, data):
    add = DoublyListNode(data)
    add.next = self.head.next
    add.prev = self.head
    self.head.next.prev = add
    self.head.next = add
    self.count += 1
    
  def add_node_at_tail(self, data):
    add = DoublyListNode(data)
    add.prev = self.tail.prev
    add.next = self.tail
    self.tail.prev.next = add
    self.tail.prev = add
    self.count += 1
  
  def remove_node_by_index(self, index):
    cur = self.head.next
    pre = self.head
    for i in range(index):
      cur = cur.next
      pre = pre.next
    nex = cur.next
    pre.next = nex
    nex.prev = pre
    cur.prev = None
    cur.next = None
  
  def remove_node_by_data(self, data):
    index = self.__index__(data)
    self.remove_node_by_index(index)
  
  def print_list(self):
    output = ''
    cur = self.head.next
    while cur:
      output += str(cur.data)+'\t'
      cur = cur.next
    print(output)

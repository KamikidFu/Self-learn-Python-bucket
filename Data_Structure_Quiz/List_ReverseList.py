#The key is the pointer trick and make it reversed

def reverse(list):
  cur = list.head
  pre = None
  nex = None
  
  while cur:
    temp = cur.next
    
    cur.next = pre
    
    pre = cur
    cur = temp
  
  list.head = pre
  return list

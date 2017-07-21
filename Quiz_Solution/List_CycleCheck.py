#Basic idea is using two markers to trace whole list and check if there is cycle
#The speed of two markers is different, make marker2 more quick than marker1
#Because let marker1 chase and catch marker2, if they meet each other
#There is a cycle in list
def cycle_check(node):
  marker1 = node
  marker2 = node
  
  while marker2 != None and marker2.next != None:
    marker1 = marker1.next
    marker2 = marker2.next.next
    
    if marker2 == marker1:
      return True
  
  return False    

#Key is that the order of queue and stack is different.
#Using two stacks to run as a queue in right order is a main solution

class Queue2Stack(object):
  def __init__(self):
    self.inStack = [] #Using tuple to consider as a temporary stack
    self.outStack = []
  
  def enqueue(self, item):
    self.inStack.append(item)
    
  def dequeue(self):
    '''
    Reversal the inStack and pop out from outStack
    '''
    if not self.outStack:
      while self.inStack:
        self.outStack.append(self.inStack.pop())
    return self.outStack.pop()
  
  def isEmpty(self):
    return (self.inStack == []) and (self.outStack == [])
    
  def size(self):
    if self.inStack == []:
      return len(self.outStack)
    else:
      return len(self.outStack)+len(self.inStack)
  
  def printQueue(self):
    output = 'IN-> '
    if self.inStack:
      index = len(self.inStack)-1
      while index > -1:
        output += str(self.inStack[index])+' '
        index -= 1
    for items in self.outStack:
      output += str(items)+' '
    
    output +='->OUT'
    print(output)

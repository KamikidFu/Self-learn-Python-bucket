#Using the idea of FILO of stack
#The solution is based on checking balance in stack

def balance_check(s):
  if len(s) == 0:
    print(True)
    return
  if len(s)%2 != 0:
    print(False)
    return
  
  left = set('{[(')
  pairs = set([('(',')'),('[',']'),('{','}')])
  
  stack = []  #Using tuple to consider as a temporary stack
  
  for bracket in s:
    if bracket in left:
      stack.append(bracket)
    else:
      if len(stack) == 0:
        print(False)
        return
      
      if(stack.pop(), bracket) not in pairs:
        print(False)
        return
  
  print(len(stack) == 0)

key_string = input("Please input any brackets for check:\n")
balance_check(key_string)

#This quiz is to reverse a string.
#Somehow in python, there is a trick way to do so as [::-1]
#However, this solution is going to do recursion to reverse a string
#And the length of string is the flag of stop

def reverse(s, output = None):
    if output is None:
        output = ''
        
    if len(s) == 1:
        return s
    else:
        return (reverse(s[1:], output) + s[0]) #s[1:] is something like s.substring() in other language

key_string = input('Please input the string to reverse:\n')
print(reverse(key_string))
        

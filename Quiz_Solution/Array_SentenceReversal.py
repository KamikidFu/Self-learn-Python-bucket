#Reverse sentence using array is going to print each words
#in a reversal order

def reversal(s1):
    '''
    output = ''
    index = len(s1)-1
    for i in s1:
        output += (s1[index])
        index -= 1

    print(output)
    '''
    output = ''
    s1 = s1.split(' ')
    index = len(s1)-1
    for i in s1:
        output += (s1[index]+" ")
        index -= 1

    print(output)
        
    
string_input = input("Please input your string:\n")
reversal(string_input)
    

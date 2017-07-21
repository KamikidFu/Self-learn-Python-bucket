#Reverse sentence using array is going to print each words
#in a reversal order

'''
#Using python abilities
def reversal_by_method(s1):
    print("".join(reversed(s1.split())))

def reversal_by_bracket(s1):
    print("".join(s1.split()[::-1]))
'''

def reversal(s1):
    '''
    output = ''
    s1 = s1.split(' ')
    index = len(s1)-1
    for i in s1:
        output += (s1[index]+" ")
        index -= 1

    print(output)
    '''

    #Manually split string to words tuple
    words = []
    length = len(s1)
    space = [' ']

    counter = 0
    
    while counter < length:
        if s1[counter] not in space:
            word_begin = counter
            while counter < length and s1[counter] not in space:
                counter += 1

            words.append(s1[word_begin:counter])

        counter += 1
        
    #Reversal the words into string
    output = ''
    index = len(words)-1
    
    while index > -1:
        
        if index != 0:
            output += (words[index]+" ")
        else:
            output += words[index]
            
        index -= 1

    print(output)

        
string_input = input("Please input your string:\n")
reversal(string_input)
    

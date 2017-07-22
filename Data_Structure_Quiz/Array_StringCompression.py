#Quiz: string like AABBCCC compress to A2B2C3
#This solution is going to use dictionary to record the characters
#and the times it appears
#More general algorithm is not to use python dictionary but using
#a counter list and marker list. Both data match each other by index

def compression(s1):

    if len(s1) == 0:
        return
    elif len(s1) == 1:
        print(s1+"1")
        return
    
    marker = []
    counter = []
    s1 = sorted(s1.replace(" ", ""))
    for i in s1:
        if i in marker:
            counter[marker.index(i)] += 1
        else:
            marker.append(i)
            counter.append(1)

            
    output = ''
    for i in marker:
        output += i + str(counter[marker.index(i)])

    print(output)
    
'''
#Using python dictionary data structure

    record = {}
    s1 = sorted(s1.replace(" ",''))
    for i in s1:
        if i in record:
            record[i] += 1
        else:
            record[i] = 1

    output = ''
    for i in record:
        output += (str(i)+str(record[i]))
    print(output)
    
'''

string_input = input("Input your string to compress:\n")
compression(string_input)
        

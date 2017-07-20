#This solution is going to use dictionary to record the characters
#and the times it appears

def compression(s1):
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

string_input = input("Input your string to compress:\n")
compression(string_input)
        

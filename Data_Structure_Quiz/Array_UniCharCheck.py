#Using python set() and len() function could easily solve this problem
#Manually do it could also under this idea

def uni_char(s):
    '''
    #Nice and simple to deal with this problem
    print(len(set(s)) == len(s))
    '''

    chars = set()

    for char in s:
        if char in chars:
            print(False)
            return
        else:
            chars.add(char)

    print(True)
    

key_string = input("Please input your string:\n")
uni_char(key_string)

#This quiz is to do operation like given a string, abc
#And output all the permutation of 'abc'
#ie. abc, acb, bac, bca, cab, cba
#The length of string is also the base case

def permute(s):
    output = []

    if len(s) == 1:
        output = [s]
    else:
        for i, letter in enumerate(s):
            print('index:'+str(i)+'Letter:'+str(letter))
            for perm in permute(s[:i] + s[i+1:]):
                print('Current permutation: '+perm)
                output += [letter+perm]
                print(output)

    return output

key_string = input('Please input your string:\n')
print(permute(key_string))


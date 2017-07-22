#This quiz is calculate the sum of input like n(n-1)(n-2)...1, 0<n<10

def sum_func(key):
    key_int = int(key[0])
    if key_int == 1:
        return key_int
    else:
        return key_int + sum_func(key[1:])

key_string = input('Please input the number:\n')
print(sum_func(key_string))

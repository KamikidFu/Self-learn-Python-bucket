#This solution to this quiz is similar to the concept of bubble sort
#Two loops in total, outside loop to go throught all the elements in array
#Inner loop to go throught No.n-1 elements in array
#Check the equality and record pairs

import pdb

'''
O(N) Solution:
'''
def pair_sum_check(int_array,int_sum):
    
    output = set()
    
    for num in int_array:
        key = int_sum - num
        if key in int_array:
            if((key, num) not in output) and ((num, key)not in output):
                output.add((key, num))
                
    print('Pair sum:\n'.join(map(str, list(output))))

'''
O(N^2) solution:
def pair_sum_check(int_array, int_sum):
    if len(int_array)<2:
        print("Array elements are less than 2")
        return
    
    record = []

    for i in int_array:
        for j in int_array:
                if (i + j) == int_sum:
                    if ((i, j) not in record) and ((j, i) not in record):
                        record.append((i, j))
    print("Pair sum:\n")
    for i in record:
        print(str(i) + "\n")     
'''

integer_array = tuple(map(int, input("Please input your integer array:\n").split(',')))
integer_sum = int(input("Please input your specific sum:\n"))
pair_sum_check(integer_array,integer_sum)

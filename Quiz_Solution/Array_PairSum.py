#This solution to this quiz is similar to the concept of bubble sort
#Two loops in total, outside loop to go throught all the elements in array
#Inner loop to go throught No.n-1 elements in array
#Check the equality and record pairs

def pair_sum_check(int_array, int_sum):
    record = []
    
    for i in int_array:
        for j in int_array:
                if (i + j) == int_sum:
                    if ((i, j) not in record) and ((j, i) not in record):
                        record.append((i, j))
 
    print("Pair sum:\n")
    for i in record:
        print(str(i) + "\n")

integer_array = tuple(map(int, input("Please input your integer array:\n").split(',')))
integer_sum = int(input("Please input your specific sum:\n"))
pair_sum_check(integer_array,integer_sum)
            

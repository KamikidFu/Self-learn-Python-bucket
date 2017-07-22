#Negative number is used as a flag.

def large_cont_sum(array):
    if len(array) == 0:
        return 0

    max_sum = current_sum = array[0]

    for num in array[1:]:
        current_sum = max(current_sum+num, num)
        max_sum = max(current_sum, max_sum)

    print(max_sum)

large_cont_sum([1,2,-1,3,4,10,10])

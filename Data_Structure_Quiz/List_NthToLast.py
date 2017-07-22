#This solution is calculate the nth to the last node
#Direct solution is that, assume the list has no cycle
#and the length of list is x, orderly, the index of nth to the last node
#is the x-n, e.g.:
#list: a, b, c, d, e
#print(1) is e, the index 4 in the list.
#The list is build by mylist.py in Data_Structure folder

def nth_to_the_last(n, input_list):
    index = len(input_list) - n
    for i in input_list:
        if index == 0:
            print(i.data)
        else:
            index -= 1
    return


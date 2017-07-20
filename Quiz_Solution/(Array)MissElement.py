#The solution to this quiz is going to use record.
#Similar to anagram check, record all the chars in string one and
#check the second string with the record. Finally output all the
#records which the number associated with is not 0

def miss_element_check(s1, s2):
    s1 = sorted(s1.replace(" ","").lower())
    s2 = sorted(s2.replace(" ","").lower())

    record_s1_to_s2 = {}
    record_s2_to_s1 = {}
    
    for char in s1:
        if char not in record_s1_to_s2:
            record_s1_to_s2[char] = 1

    for char in s2:
        if char in record_s1_to_s2:
            record_s1_to_s2[char] = 0
        else:
            record_s2_to_s1[char] = 1

    print("Compared 1st string, the 2nd string is missing:\n")
    for key in record_s1_to_s2:
        if record_s1_to_s2[key] != 0:
            print(key + "\n")

    print("Compared 2nd string, the 1st string is missing:\n")
    for key in record_s2_to_s1:
        if record_s2_to_s1[key] != 0:
            print(key + "\n")    

key_string_1 = input("Please input your 1st string:\n")
key_string_2 = input("Please input your 2nd string:\n")
miss_element_check(key_string_1, key_string_2)    

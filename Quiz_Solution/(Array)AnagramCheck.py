#There could be at least two solutions to anagram check

#1. After replace all the space and make characters to lower case,
#then sort it out to check if they are the same.

#2. After replace all the space and make characters to lower case,
#then record all the characters in one string and check the other
#string if its characters are all in record.

#take two arguments, string 1 and string 2
def anagram_check_by_sort(s1, s2):
    s1 = sorted(s1.replace(" ","").lower())
    s2 = sorted(s2.replace(" ","").lower())
    if s1 == s2:
        print("(Sort Method) True Anagram")
        return
    print("(Sort Method) False Anagram")

def anagram_check_with_record(s1, s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()
    if len(s1) != len(s2):
        print("(Record Method) False Anagram")
        return
    record = {} #Using dictionary
    for char in s1:
        if(char in record):
            record[char] += 1
        else:
            record[char] = 1

    for char in s2:
        if char in record:
            record[char] -= 1
        else:
            record[char] = 1

    for char in record:
        if record[char] != 0:
            print("(Record Method) False Anagram")

    print("(Record Method) True Anagram")
    

key_string_1 = input("Please input your 1st string:\n")
key_string_2 = input("Please input your 2nd string:\n")
anagram_check_by_sort(key_string_1,key_string_2)
anagram_check_with_record(key_string_1,key_string_2)

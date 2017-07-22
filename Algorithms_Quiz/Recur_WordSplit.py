#Split method has input, no matter a pattern or using regular expression
#Using recursion to split a string to sentence basically is to use each
#pattern as a input in split method and form a final output

def word_split(phrase, list_of_word, output = None):
    if output is None:
        output = []

    for word in list_of_word:
        if phrase.startswith(word):
            output.append(word)

            return word_split(phrase[len(word):],list_of_word,output)

    return output


key_string = input('Please input your string:\n')
key_list = input('Please input your word list, devided by comma \',\':\n').split(',')
print(word_split(key_string, key_list))

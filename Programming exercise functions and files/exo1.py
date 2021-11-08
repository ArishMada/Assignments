import os
import string

def hapax_finder():
    filename = input('Enter the name of the file (filename.txt): ')
    file = open(os.getcwd()+'\\'+filename, 'r')
    text = file.read().lower().replace('\ni', '')
    text1 = ""
    for punctuation in text:
        if punctuation not in string.punctuation:
           text1 += punctuation
    text = text1
    list1 = text.split()
    list_of_words = {}
    for i in list1:
        if i not in list_of_words:
           list_of_words[i] = 1
        else:
           list_of_words[i] += 1
    newd = []
    for i in list_of_words:
        if list_of_words[i] == 1:
            newd.append(i)
    for word in newd:
        print(word)

hapax_finder()


import os
import string


def average_word_length():
    filename = input('Enter the name of the file (filename.txt): ')
    file = open(os.getcwd() + '\\' + filename, 'r')
    # make a list of words
    lst = file.read().split()
    # remove the punctuations
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in lst]
    # calculate the sum of the lengths
    sum = 0
    for i in stripped:
        sum += len(i)
    print(f'sum of all the words lengths is {sum}')
    # get the number of words
    number_of_words = len(stripped)
    print(f'There are {number_of_words} words in this text.')
    # calculate the average length
    average = sum / number_of_words
    # format the result because it might be an irrational number
    average = "{:.3f}".format(average)
    print(f'The average word length in this text is {average}')


average_word_length()

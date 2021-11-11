import os


def sentences_splitter():
    global next_elem
    filename = input('Enter the name of the file (filename.txt): ')
    file = open(os.getcwd() + '\\' + filename, 'r')
    input_text = file.read().split()
    formatted_text = ""
    title = ['Dr.', 'Esq.', 'Hon.', 'Jr.', 'Mr.', 'Mrs.', 'Ms.']
    etc = '...'
    n = len(input_text)

    for i in input_text:
        p = input_text.index(i)
        if p < n - 1:
            next_elem = input_text[p + 1]
        if '?' in i or '!' in i and next_elem[0].isupper():
            formatted_text += (i + "\n")
        elif '.' in i[-1] and i not in title and i.count('.') == 1 and next_elem[0].isupper():
            formatted_text += (i + "\n")
        elif etc in i:
            formatted_text += (i + "\n")
        else:
            formatted_text += (i + " ")

    print(formatted_text)


sentences_splitter()

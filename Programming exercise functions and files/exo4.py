import os


def sentences_splitter():
    filename = input('Enter the name of the file (filename.txt): ')
    file = open(os.getcwd() + '\\' + filename, 'r')
    input_text = file.read().split()
    print(input_text)
    formatted_text = ""
    title = ['Dr.', 'Esq.', 'Hon.', 'Jr.', 'Mr.', 'Mrs.', 'Ms.']
    etc = '...'
    for i in input_text:
        if '?' in i or '!' in i:
            formatted_text += (i + "\n")
        elif '.' in i[-1] and i not in title and i.count('.') == 1:
            formatted_text += (i + "\n")
        elif etc in i:
            formatted_text += (i + "\n")
        else:
            formatted_text += (i + " ")

    print(formatted_text)


sentences_splitter()

import os


def numbered_sentences():
    filename = input('Enter the name of the file (filename.txt): ')
    file = open(os.getcwd() + '\\' + filename, 'r')
    content = list(file.read().split('\n'))
    count = 1
    for i in content:
        if i != '':
            print(f'{count}:{i}')
            count += 1
    file.close()


numbered_sentences()

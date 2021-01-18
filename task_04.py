some_str = input('Введите несколько слов, разделенных пробелами: ')
words_list = some_str.split(' ')
for i, el in enumerate(words_list, 1):
    print(i, el[:10])

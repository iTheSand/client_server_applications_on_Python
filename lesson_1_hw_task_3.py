# Задача 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
bytes_str_in_lst = ['attribute', 'класс', 'функция', 'type']

for bytes_s in bytes_str_in_lst:
    try:
        print(bytes(bytes_s, 'ascii'))
    except UnicodeEncodeError:
        print(f'Слово {bytes_s} невозможно записать в байтовом типе!')

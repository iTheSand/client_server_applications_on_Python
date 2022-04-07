# Задача 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
bytes_s_in_lst = [b'class', b'function', b'method']
for bytes_s in bytes_s_in_lst:
    print(bytes_s, type(bytes_s), len(bytes_s))



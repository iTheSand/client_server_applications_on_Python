# Задача 1. Задание на закрепление знаний по модулю CSV.
# Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt
# и формирующий новый «отчетный» файл в формате CSV.
# Для этого:
# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
# В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
# «Изготовитель системы»,  «Название ОС», «Код продукта», «Тип системы».
# Значения каждого параметра поместить в соответствующий список.
# Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
# В этой же функции создать главный список для хранения данных отчета — например,
# main_data — и поместить в него названия столбцов отчета в виде списка:
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);

# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
# В этой функции реализовать получение данных через вызов функции get_data(),
# а также сохранение подготовленных данных в соответствующий CSV-файл;

# Проверить работу программы через вызов функции write_to_csv().
import csv
import re


def get_data():
    param_name = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data = [param_name]
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    for i in range(1, 4):
        count = 1
        with open(f'info_{i}.txt', 'r') as file:
            text = file.read()
            for word in param_name:
                search_line = ''.join(re.findall(f'{word}:\s+.+', text))
                result = (re.split(':\s+', search_line)[1])
                if count == 1:
                    os_prod_list.append(result)
                elif count == 2:
                    os_name_list.append(result)
                elif count == 3:
                    os_code_list.append(result)
                else:
                    os_type_list.append(result)
                count += 1
    for n in range(0, 3):
        if n == 0:
            os_param_1 = [os_prod_list[n], os_name_list[n], os_code_list[n], os_type_list[n]]
            main_data.append(os_param_1)
        elif n == 1:
            os_param_2 = [os_prod_list[n], os_name_list[n], os_code_list[n], os_type_list[n]]
            main_data.append(os_param_2)
        else:
            os_param_3 = [os_prod_list[n], os_name_list[n], os_code_list[n], os_type_list[n]]
            main_data.append(os_param_3)
    return main_data


def write_to_csv(csv_file):
    result = get_data()
    with open(csv_file, 'w', encoding='utf-8') as csv_f:
        csv_writer = csv.writer(csv_f)
        for row in result:
            csv_writer.writerow(row)
        print(f'CSV-файл ({csv_file}) - записан!')


write_to_csv('lesson_2_hw_task_1.csv')

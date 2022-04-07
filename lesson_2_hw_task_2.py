# Задача 2. Задание на закрепление знаний по модулю json.
# Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными.
# Для этого:
# Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item),
# количество (quantity), цена (price), покупатель (buyer), дата (date).
# Функция должна предусматривать запись данных в виде словаря в файл orders.json.
# При записи данных указать величину отступа в 4 пробельных символа;

# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
import json


def write_order_to_json(item, quantity, price, buyer, date):
    dict_to_json = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }
    with open('orders.json') as json_file:
        json_objects = json.load(json_file)
        for key, value in json_objects.items():
            value.append(dict_to_json)

    with open('orders.json', 'w', encoding='utf-8') as json_f:
        json.dump(json_objects, json_f, indent=4)

    print('JSON-файл дозаписан!')


write_order_to_json('prod3', 2, 790, 'Pavel', '11-05-2021')

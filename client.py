from socket import *
import sys
import os
import time
import json


def client():
    argv = sys.argv[1:]

    try:
        ip_addr = argv[0]
    except (UnboundLocalError, IndexError) as e:
        ip_addr = 'localhost'
        print('Параметры командной строки скрипта client.py <addr> [<port>]'.format(e.args[-1]))

    try:
        port_default = int(argv[1][1:5])
    except IndexError:
        port_default = 7777

    acc_name = os.environ.get('USERNAME')
    time_str = time.strftime('%d.%m.%Y %H:%M:%S')
    presence_message = {
        "action": "presence",
        "time": time_str,
        "type": "status",
        "user": {
            "account_name": acc_name,
            "status": "Yep, I am here!"
        }
    }

    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.connect((ip_addr, port_default))
    except ConnectionRefusedError:
        print('Подключение недоступно!')

    msg_to_server = presence_message
    s.send(json.dumps(msg_to_server).encode('utf-8'))
    data = s.recv(1024)
    decoded_data = json.loads(data.decode('utf-8'))
    for a, b in decoded_data.get("response").items():
        if a == '1xx':
            for x, y in b.items():
                if x == '100':
                    print(f'{int(x)} - {y} ({time_str})')

    s.close()


client()

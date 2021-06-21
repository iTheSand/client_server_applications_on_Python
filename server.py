from socket import *
import sys
import time
import json


def server():
    argv = sys.argv[1:]

    try:
        ip_addr = argv[1]
    except (UnboundLocalError, IndexError) as e:
        print('Параметры командной строки скрипта server.py -a <addr> -p <port>'.format(e.args[-1]))

    try:
        port_default = int(argv[3])
    except IndexError:
        port_default = 7777

    time_str = time.strftime('%d.%m.%Y %H:%M:%S')

    response_to_client = {
        "response":
            {"1xx": {
                100: "Presence message received!",
                101: "Receiving error!"}},
        "time": time_str
    }

    s = socket(AF_INET, SOCK_STREAM)
    s.bind((ip_addr, port_default))
    s.listen(5)

    while True:
        client, addr = s.accept()
        data = client.recv(1024)
        decoded_data = json.loads(data.decode('utf-8'))
        if decoded_data.get("action") == "presence":
            print(
                f'Message from {decoded_data.get("user").get("account_name")}: {decoded_data.get("user").get("status")}')
            print(f'Received {decoded_data.get("time")}')
            msg_to_client = response_to_client
            client.send(json.dumps(msg_to_client).encode('utf-8'))
            client.close()
        else:
            print(f'Another message from the client')


server()

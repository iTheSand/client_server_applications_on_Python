# Задача 1. Реализовать обработку нескольких клиентов на сервере, используя функцию select.
# Клиенты должны общаться в «общем чате»: каждое сообщение участника отправляется всем, подключенным к серверу.
from socket import socket, AF_INET, SOCK_STREAM
import time


def client():
    address = ('localhost', 8888)
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(address)

    while True:
        start = time.time()
        mode = input('listening mode - L + enter, message mode - M + enter: ')
        if mode == 'L':
            while True:
                if time.time() - start > 30:
                    break
                else:
                    data = s.recv(1024).decode('utf-8')
                    print(f'Message: ', data)
        elif mode == 'M':
            while True:
                message = input('Enter your message (exit - E + enter): ')
                if message == 'E':
                    break
                else:
                    s.send(message.encode('utf-8'))
        else:
            print('enter the correct operating mode')


if __name__ == '__main__':
    client()

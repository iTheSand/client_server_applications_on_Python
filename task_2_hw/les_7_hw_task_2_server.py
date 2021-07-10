# Задача 2. Реализовать функции отправки/приема данных на стороне клиента.
# Чтобы упростить разработку на данном этапе, пусть клиентское приложение будет либо только принимать,
# либо только отправлять сообщения в общий чат. Эти функции надо реализовать в рамках отдельных скриптов.
import select
from socket import socket, AF_INET, SOCK_STREAM


def read_req_and_write_resp(r_clients, w_clients, clients):
    for r_sock in r_clients:
        try:
            data = r_sock.recv(1024)
            for w_sock in w_clients:
                try:
                    w_sock.send(data)
                except:
                    clients.remove(w_sock)
        except:
            pass


def main():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', 8888))
    sock.listen(5)
    sock.settimeout(0.2)

    clients = []

    while True:
        try:
            conn, addr = sock.accept()
        except OSError:
            pass
        else:
            clients.append(conn)
        r = []
        w = []
        e = []
        try:
            r, w, e = select.select(clients, clients, [], 0)
        except OSError:
            pass

        read_req_and_write_resp(r, w, clients)


if __name__ == '__main__':
    main()

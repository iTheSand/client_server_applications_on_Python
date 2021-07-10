# Задача 1. Реализовать обработку нескольких клиентов на сервере, используя функцию select.
# Клиенты должны общаться в «общем чате»: каждое сообщение участника отправляется всем, подключенным к серверу.
import select
from socket import socket, AF_INET, SOCK_STREAM


# чтение запросов
def read_requests(r_clients, clientslist):
    responses = {}

    for sock in r_clients:
        try:
            data = sock.recv(1024).decode('utf-8')
            responses[sock] = data
        except:
            clientslist.remove(sock)

    return responses


# ответы клиентам на запросы
def write_responses(requests, w_clients, clients):
    for sock in w_clients:
        if sock in requests:
            try:
                resp = requests[sock].encode('utf-8')
                for cl in w_clients:
                    if cl != sock:
                        cl.send(resp)
            except:
                sock.close()
                clients.remove(sock)


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

        w = []
        r = []
        e = []
        try:
            r, w, e = select.select(clients, clients, [], 0)
        except OSError:
            pass

        requests_list = read_requests(r, clients)
        if requests_list:
            write_responses(requests_list, w, clients)


if __name__ == '__main__':
    main()

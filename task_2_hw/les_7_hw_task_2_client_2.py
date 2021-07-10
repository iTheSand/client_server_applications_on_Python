from socket import socket, AF_INET, SOCK_STREAM

address = ('localhost', 8888)
s = socket(AF_INET, SOCK_STREAM)
s.connect(address)

while True:
    data = s.recv(1024).decode('utf-8')
    print(f'Message: ', data)


from socket import socket, AF_INET, SOCK_STREAM

address = ('localhost', 8888)
s = socket(AF_INET, SOCK_STREAM)
s.connect(address)

while True:
    message = input('Enter your message: ')
    s.send(message.encode('utf-8'))

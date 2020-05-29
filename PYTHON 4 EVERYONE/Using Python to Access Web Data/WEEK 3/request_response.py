import socket

pathway = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pathway.connect(('data.pr4e.org', 80))
data_file = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n'.encode()
pathway.send(data_file)

while True:
    data = pathway.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end=" ")

pathway.close()

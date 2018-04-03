import socket
import sys

infos = socket.getaddrinfo('127.0.0.1', 3000)
stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]
client = socket.socket(*stream_info[:3])

client.connect(stream_info[-1])

message = ''

for item in sys.argv[1:-1]:
    message += item
    message += ' '

message += sys.argv[-1]

client.sendall(message.encode('utf8'))

buffer_length = 8
message_complete = False
thing = ''

while not message_complete:
    part = client.recv(buffer_length)
    thing += part.decode('utf8')
    if len(part) < buffer_length:
        message_complete = True

print(thing)

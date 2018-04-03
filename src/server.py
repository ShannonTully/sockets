import socket
import datetime as dt

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_TCP)

address = ('127.0.0.1', 3000)

sock.bind(address)

sock.listen(1)

print("--- Starting server on port 8888 at {} ---".format(dt.datetime.now()))

conn, addr = sock.accept()

buffer_length = 8
message_complete = False
thing = 'Message: '

while not message_complete:
    part = conn.recv(buffer_length)
    thing += part.decode('utf8')
    if len(part) < buffer_length:
        message_complete = True

conn.sendall(thing.encode('utf8'))

print('[{}] {}'.format(dt.datetime.now(), thing))

print("--- Stopping server on port 8888 at {} ---".format(dt.datetime.now()))

conn.close()
sock.close()

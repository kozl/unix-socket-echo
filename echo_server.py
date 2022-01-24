#!/usr/bin/env python3

import os
import socket
import time

socket_path = os.path.join(os.environ['ECHO_SERVER_DIR'], 'echo.socket')

# удаляем сокет-файл, если он существует (чтобы случайно не переиспользовать существующий)
if os.path.exists(socket_path):
    os.remove(socket_path)

# socket создёт сокет, socket.AF_UNIX и socket.SOCK_STREAM (family и type) используются для создания unix-сокета
# https://docs.python.org/3/library/socket.html#socket.socket
with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
    # sock.bind используется для привезки сокета к сокет файлу в socket_path
    # https://docs.python.org/3/library/socket.html#socket.socket.bind
    sock.bind(socket_path)
    # sock.listen используется для того чтобы переключить сокет в режим приёма соединений
    # https://docs.python.org/3/library/socket.html#socket.socket.listen
    sock.listen()
    while True:
        # sock.accept блокируется и возвращает пару (conn, addr), где conn — установленное
        # соединение, которое можно использовать для приёма и отправки данных, addr опускаем за ненадобностью
        # https://docs.python.org/3/library/socket.html#socket.socket.accept
        conn, _ = sock.accept()
        # conn.recv возвращает данные переданные серверу в сокет (1024 — максимальный размер данных, которые будут приняты за раз)
        # https://docs.python.org/3/library/socket.html#socket.socket.recv
        data = conn.recv(1024)
        # conn.send отправляет данные обратно в сокет
        # https://docs.python.org/3/library/socket.html#socket.socket.send
        conn.send(data)
        conn.close()

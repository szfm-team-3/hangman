import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(1024).decode()
        if not data:
            print('Itt a vege')
            break
        data = data.split('|')
        if data[0] == 'VARAKOZAS':
            print('Várakozás a másik játékosra...')
        elif data[0] == 'IRJVALAMIT':
            if data[1]:
                print('< ' + data[1])
            sent = input('> ')
            s.sendall(sent.encode())
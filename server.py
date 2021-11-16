import socket

HOST = '127.0.0.1'
PORT = 65432

class Player:
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr

def test_msg(active, passive):
    data = passive.conn.recv(1024).decode()
    active.conn.sendall(('IRJVALAMIT|' + data).encode())
    passive.conn.sendall(b'VARAKOZAS|')
    return data

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print('Server has started...')
    s.listen()
    conn, addr = s.accept()
    p1 = Player(conn, addr)
    with p1.conn:
        print('Connected to', p1.addr)
        p1.conn.sendall(b'VARAKOZAS|')
        conn, addr = s.accept()
        p2 = Player(conn, addr)
        with p2.conn:
            print('Connented to', p2.addr)
            p2.conn.sendall(b'IRJVALAMIT|')
            while True:
                if not test_msg(p1, p2):
                    break
                if not test_msg(p2, p1):
                    break
            print('Itt a vege')
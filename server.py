import socket
import random

HOST = '127.0.0.1'
PORT = 65432

class Player:
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        self.sentence = ''
        self.good_letters = []
        self.wrong_letters = []
        self.encoded_sentence = ''
        
    def is_guessed(self, sentence):
        for l in sentence:
            if l not in self.good_letters and l != ' ':
                return False
        return True
    
    def encode_sentence(self, sentence):
        self.encoded_sentence = ''
        for l in sentence:
            if l in self.good_letters:
                self.encoded_sentence += l
            elif l == ' ':
                self.encoded_sentence += ' '
            else:
                self.encoded_sentence += '#'

def get_sentence(passive, active):
    passive.conn.sendall(b'MONDATBEKERES|')
    active.conn.sendall(b'VARAKOZAS|')
    passive.sentence = passive.conn.recv(1024).decode()
    
def is_guessing_ended(active, passive):
    if len(active.wrong_letters) >= 6 or active.is_guessed(passive.sentence):
        return True
    
def start_guessing(active, passive):
    while True:
        active.encode_sentence(passive.sentence)
        wrong_letters = ''.join(active.wrong_letters)
        active.conn.sendall(('BETUBEKERES|' + wrong_letters + '|' + active.encoded_sentence).encode())
        passive.conn.sendall(('VARAKOZAS|' + wrong_letters + '|' + active.encoded_sentence).encode())
        letter = active.conn.recv(1024).decode()
        
        if letter in passive.sentence:
            active.good_letters.append(letter)
        else:
            active.wrong_letters.append(letter)
        
        if is_guessing_ended(active, passive):
            break

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
            get_sentence(p2, p1)
            start_guessing(p1, p2)
            get_sentence(p1, p2)
            start_guessing(p2, p1)
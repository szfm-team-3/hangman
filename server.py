import socket
import random

HOST = '192.168.0.191'
PORT = 65432

class Player:
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        self.sentence = ''
        self.good_letters = []
        self.wrong_letters = []
        self.encoded_sentence = ''
        self.score = 0
        
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
    if len(active.wrong_letters) >= 6:
        active.score -= 1
        passive.score += 1
        return True
    if active.is_guessed(passive.sentence):
        active.score += 1
        passive.score -= 1
        return True
    return False
    
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
            wrong_letters = ''.join(active.wrong_letters)
            active_score = str(active.score) + 'X' + str(passive.score)
            passive_score = str(passive.score) + 'X' + str(active.score)
            active.conn.sendall(('FORDULOVEGE|' + wrong_letters + '|' + active.encoded_sentence + '|' + active_score).encode())
            passive.conn.sendall(('FORDULOVEGE|' + wrong_letters + '|' + active.encoded_sentence + '|' + passive_score).encode())
            break
        
def end_screen(p1, p2):
    p1_gameend_status = str(p1.score) + 'X' + str(p2.score)
    p2_gameend_status = str(p2.score) + 'X' + str(p1.score)
    p1.conn.sendall(('JATEKVEGE|' + '|' + p1_gameend_status).encode())
    p2.conn.sendall(('JATEKVEGE|' + '|' + p2_gameend_status).encode())

while True:
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
                end_screen(p1, p2)
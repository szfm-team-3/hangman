import socket
from graphic import *

HOST = '127.0.0.1'
PORT = 65432

abc = 'AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ'

def is_valid_word(word):
    if len(word) < 5 or len(word) > 20:
        return False
    for i in word:
        if i not in abc and i != ' ':
            return False
    return True 

def is_valid_letter(letter, data):
    if len(letter) == 1 and letter in abc and letter not in (data[1]+data[2]):
        return True
    return False

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(1024).decode()
        if not data:
            print('Itt a vege')
            break
        data = data.split('|')
        act_state = len(data[1])
        if data[0] == 'VARAKOZAS':
            if len(data) == 3:
                redraw(act_state)
                print()
                print('Hibás betűk: ', data[1])
                print('Szó:', data[2])
                print('--- ELLENFÉL KÖRE ---')
            else:
                redraw(-1)
                print('Várakozás a másik játékosra...')
            continue
        elif data[0] == 'MONDATBEKERES':
            redraw(-1)
            while True:
                print('Adj meg egy mondatot.\nCsak betűkből és szóközökből, legalább 5, de maximum 20 karakterből állhat!')
                word = input('> ')
                word = ' '.join(word.split()).strip().upper()
                if is_valid_word(word):
                    s.sendall(word.encode())
                    break;
                else:
                    redraw(-1)
                    print('Nem érvényes mondat!')
        elif data[0] == 'BETUBEKERES':
            redraw(act_state)
            while True:
                print('Hibás betűk: ', data[1])
                print('Szó:', data[2])
                print('Adj meg egy betűt!')
                letter = input('> ')
                letter = letter.strip().upper()
                if is_valid_letter(letter, data):
                    s.sendall(letter.encode())
                    break
                else:
                    redraw(act_state)
                    print('Nem érvényes betű!')
import socket
from graphic import *
import time

HOST = '127.0.0.1'
HOST = socket.gethostbyname('szgyula.tplinkdns.com')
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

def start_game():
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
            elif data[0] == 'FORDULOVEGE':
                redraw(act_state)
                score = data[3].split('X')
                print('Eredmény:')
                print('A te pontod: ' + score[0])
                print('Ellenfél pontja: ' + score[1])
                print('Forduló vége - 10 másodperc pihi')
                time.sleep(10)
            elif data[0] == 'JATEKVEGE':
                redraw(-1)
                score = data[2].split('X')
                
                print('Játék vége:')
                print('A te pontod: ' + score[0])
                print('Ellenfél pontja: ' + score[1])
                score[0] = int(score[0])
                score[1] = int(score[1])
                
                if score[0] > score[1]:
                    print('Te nyertél! Gratulálok!')
                elif score[0] < score[1]:
                    print('Sajnos most te vesztettél, de ne add fel legközelebb te fogsz győzni!')
                else:
                    print('Hú ez nagyon szoros lett, ez a meccs döntetlen lett!')
                time.sleep(10)
                os.system(clearcmd)
                        


os.system(clearcmd)
while (True):
    print(logo)
    print(menu)
    in_num = input("\n\tPlease make a selection from: 1, 2, 3: ")
    if len(in_num) == 1 and in_num[0].isdigit():
        if in_num == "1":
            start_game()
        elif in_num == "2":
            os.system(clearcmd)
            print(developers)
        elif in_num == "3":
            break
        else:
            os.system(clearcmd)
            print("Nincs ilyen lehetőség!")
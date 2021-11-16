import platform
import os
import time

HANGMANIMGS = ['''''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def redraw(state_num):
    clearcmd = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(clearcmd)
    print(HANGMANIMGS[state_num+1])
    
def teszt_kirajzol():
    for i in range(-1, 7):
        redraw(i)
        time.sleep(1)
        
#teszt_kirajzol()
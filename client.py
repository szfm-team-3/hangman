abc = 'AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ'

def redraw(status):
    pass

def is_valid_word(word):
    if len(word) < 5 or len(word) > 20:
        return False
    for i in word:
        if i not in abc and i != ' ':
            return False
    return True 

def is_valid_letter(letter, data):
    if len(letter) == 1 and letter in abc and letter not in (data):
        return True
    return False

def test_word():
    while True:
        print('Adj meg egy mondatot.\nCsak betűkből és szóközökből, legalább 5, de maximum 20 karakterből állhat!')
        word = input('> ')
        word = ' '.join(word.split()).strip().upper()
        if is_valid_word(word):
            print(word) # szó elküldése
            break;
        else:
            redraw(0)
            print('Nem érvényes mondat!')
    
def test_letter():
    redraw(0)
    bad_letters = "ABC"
    secret_sentence = "K#SKuTY#"
    
    while True:
        print('Hibás betűk: ', bad_letters)
        print('Szó:', secret_sentence)
        print('Adj meg egy betűt!')
        letter = input('> ')
        letter = letter.strip().upper()
        print(bad_letters + secret_sentence)
        if is_valid_letter(letter, bad_letters + secret_sentence): # titkosított mondat + rossz betűk összefűzve
            print(letter) # betű elküldése
            break
        else:
            redraw(0)
            print('Nem érvényes betű!')

#test_word()

test_letter()
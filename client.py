#!/usr/bin/python3

import os
import sys

class HangMan(object):
    hang = []
    hang.append(' +---+')
    hang.append(' |   |')
    hang.append('     |')
    hang.append('     |')
    hang.append('     |')
    hang.append('     |')
    hang.append('=======')

    man = {}
    man[0] = [' 0   |']
    man[1] = [' 0   |', ' |   |']
    man[2] = [' 0   |', '/|   |']
    man[3] = [' 0   |', '/|\\  |']
    man[4] = [' 0   |', '/|\\  |', '/    |']
    man[5] = [' 0   |', '/|\\  |', '/ \\  |']

    pics = []

    def __init__(self, *args, **kwargs):
        i, j = 2, 0
        self.pics.append(self.hang[:])
        for ls in self.man.values():
            pic, j = self.hang[:], 0
            for m in ls:
                pic[i + j] = m
                j += 1
            self.pics.append(pic)

    def getPic(self, idx, wordLen):
        output = ""
        for line in self.pics[idx]:
            output += line + "\r\n"

        return output

    #def validate(self, word, result, missed):

    def start(self):
        clear  = lambda: os.system('clear')
        i      = 0
        word   = "teszt"

        #output = 'The word is: ' + result
        output = ""

        while i < len(self.pics):
            clear()
            output = self.getPic(i, len(word)) + "\r\n" ' '

            print(output)
            inputVal = input("Adj meg egy betűt:\n")
            print(inputVal)
            i += 1
        exit(0)


a = HangMan().start()
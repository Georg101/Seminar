#!/usr/bin/env python3

morse = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.',
         'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---',
         'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---',
         'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
         'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-',
         'y':'-.--', 'z':'--..', ' ':''}

text = 'ahoj'
for pismeno in text:
    print(morse[pismeno], end='/')
print('/')

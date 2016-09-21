#!/usr/bin/python
import sys
from string_xor import string_xor
from character_frequency import *

def best_xor_key(message, frequency_filename = 'freq.dat'):
    best_key = -1
    max_score = 0.0
    for key in range(0, 256):
        score = english_score(string_xor(message, key), frequency_filename)
        if score > max_score:
            max_score = score
            best_key = key
    return best_key

def main(args):
    if len(args) < 1:
        print("Please supply some text!")
        return

    enc = args[0].decode('hex')
    key = best_xor_key(enc)
    print('Key: {}'.format(key))
    print('Unencrypted message: {}'.format(string_xor(enc, key)))

if __name__ == '__main__':
    main(sys.argv[1:])

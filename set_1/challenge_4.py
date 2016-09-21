#!/usr/bin/python
import sys
from string_xor import string_xor
from character_frequency import *

def best_xor(message, frequency_filename = 'freq.dat'):
    best_key = -1
    max_score = 0.0
    for key in range(0, 256):
        score = english_score(string_xor(message, key), frequency_filename)
        if score > max_score:
            max_score = score
            best_key = key
    return (max_score, best_key)

def main(args):
    if len(args) < 1:
        print("Please include a filename to analyze!")
        return

    best_score = 0.0
    best_line = ''
    with open(args[0]) as file:
        for line in file.read().split('\n'):
            message = line.decode('hex')
            score, key = best_xor(message)
            if score > best_score:
                best_score = score
                best_line = string_xor(message, key)
    print(best_line)

if __name__ == '__main__':
    main(sys.argv[1:])

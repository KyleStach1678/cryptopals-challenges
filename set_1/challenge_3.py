#!/usr/bin/python
import sys
from string_xor import string_xor
from character_frequency import *

def main(args):
    if len(args) < 1:
        print("Please supply some text!")
        return

    enc = args[0].decode('hex')
    _, key = best_xor(enc)
    print('Key: {}'.format(key))
    print('Unencrypted message: {}'.format(string_xor(enc, key)))

if __name__ == '__main__':
    main(sys.argv[1:])

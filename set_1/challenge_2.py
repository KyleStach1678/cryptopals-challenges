#!/usr/bin/python
import sys
from string_xor import string_xor

def main(args):
    if len(args) < 2:
        print('Usage: ./challenge_2.py <message> <key>')
        return

    message = args[0].decode('hex')
    key = args[1].decode('hex')

    # XOR Each byte of the message and the key
    encoded = string_xor(message, key)
    print(encoded.encode('hex'))

if __name__ == '__main__':
    main(sys.argv[1:])

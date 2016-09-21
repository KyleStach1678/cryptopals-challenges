#!/usr/bin/python
import sys
from string_xor import string_xor

def main(args):
    if len(args) < 2:
        print("Usage: ./challenge_5.py <key> <text>")
        return

    print(string_xor(args[1], args[0]).encode('hex'))

if __name__ == '__main__':
    main(sys.argv[1:])

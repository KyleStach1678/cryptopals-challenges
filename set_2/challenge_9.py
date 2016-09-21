#!/usr/bin/python
import sys
from padding import pad

def main(args):
    if len(args) < 2:
        print("Usage: ./challenge_1.py <text> <bytes>")
        return
    
    print(pad(args[0], int(args[1])))

if __name__ == '__main__':
    main(sys.argv[1:])

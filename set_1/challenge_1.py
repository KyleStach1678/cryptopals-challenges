#!/usr/bin/python
import sys

def main(args):
    if len(args) < 1:
        print("Please supply an argument")
        return
    print(args[0].decode('hex').encode('base64'))

if __name__ == '__main__':
    main(sys.argv[1:])

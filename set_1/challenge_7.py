#!/usr/bin/python
import sys
from Crypto.Cipher import AES

def main(args):
    if len(args) < 2:
        print("Please include a filename and a key!")
        return

    aes = AES.new(args[1], AES.MODE_ECB)

    with open(args[0]) as file:
        data = ''.join(file.readlines()).decode('base64')
        print(aes.decrypt(data))

if __name__ == '__main__':
    main(sys.argv[1:])

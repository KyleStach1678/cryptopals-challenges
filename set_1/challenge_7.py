#!/usr/bin/python
import sys
from Crypto.Cipher import AES
from Crypto import Random

def main(args):
    if len(args) < 2:
        print("Please include a filename and a key!")
        return

    IV = Random.new().read(16)
    aes = AES.new(args[1], AES.MODE_ECB, IV)

    with open(args[0]) as file:
        data = ''.join(file.readlines()).decode('base64')
        print(aes.decrypt(data))

if __name__ == '__main__':
    main(sys.argv[1:])

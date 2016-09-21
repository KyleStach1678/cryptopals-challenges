#!/usr/bin/python
import sys
from Crypto.Cipher import AES
from Crypto import Random

# A cipher text is likely encrypted with ECB if it repeats the same 16-byte sequence twice
def is_ecb(encrypted):
    repeated_count = 0
    for i in range(0, len(encrypted) / 16):
        block = encrypted[i*16:i*16+16]
        for j in range(i+1, len(encrypted) / 16):
            block_cmp = encrypted[j*16:j*16+16]
            if block == block_cmp:
                return True
    return False

def main(args):
    if len(args) < 1:
        print("Please supply a filename!")
        return

    with open(args[0]) as file:
        for hex in file.read().split('\n'):
            enc = hex.decode('hex')
            if is_ecb(enc):
                print(enc.encode('hex'))

if __name__ == '__main__':
    main(sys.argv[1:])

#!/usr/bin/python
import sys
import random
from Crypto.Cipher import AES
from Crypto import Random
from padding import pad
import time
from challenge_11 import detect_mode

def encrypt_ecb(plaintext, aes):
    text = plaintext + 'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK'.decode('base64')
    return aes.encrypt(pad(text, 16))

def main(args):
    aes = AES.new('deadbeefdeadbea713371234d34db33f'.decode('hex'), AES.MODE_ECB)

    # Find the block size
    i = 10
    size = len(encrypt_ecb('A' * i, aes))
    while len(encrypt_ecb('A' * i, aes)) == size:
        i += 1
        block_size = len(encrypt_ecb('A' * i, aes)) - size

    # Make sure it's ECB
    enc = encrypt_ecb('A' * 64, aes)
    is_ecb = (detect_mode(enc) == 'ecb')
    assert(is_ecb)

    # What we have discovered at the end of the key
    key_progress = ''
    # This doesn't actually have to be equal to the size, just greater than it
    hidden_size = block_size * 10

    # Solve for the hidden text one character at a time from the end:
    # AA...A#, AA...A##, etc
    for n in range(1, hidden_size + 1):
        n_bytes_short = 'A' * (hidden_size - n)
        output = encrypt_ecb(n_bytes_short, aes)
        # For each possible value
        for i in range(0, 256):
            # key = AAA...AA + Solved part of key + Iterated character
            key = n_bytes_short + key_progress + chr(i)
            enc = encrypt_ecb(''.join(key), aes)
            if enc[:hidden_size] == output[:hidden_size]:
                key_progress += chr(i)
                break

    print(key_progress)

if __name__ == '__main__':
    main(sys.argv[1:])

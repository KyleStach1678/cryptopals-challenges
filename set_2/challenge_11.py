#!/usr/bin/python
import sys
import random
from Crypto.Cipher import AES
from Crypto import Random
from padding import pad
import time

def generate_key():
    return Random.get_random_bytes(16)

def cbc_or_ecb(plaintext):
    use_cbc = random.randint(0, 2) == 1

    aes = AES.new(
            generate_key(),
            AES.MODE_CBC if use_cbc else AES.MODE_ECB,
            Random.get_random_bytes(16))
    text = pad(
            Random.get_random_bytes(6 + random.randint(0, 5)) +
                plaintext +
                Random.get_random_bytes(6 + random.randint(0, 5)),
            16)
    return (aes.encrypt(text), 'cbc' if use_cbc else 'ecb')

def detect_mode(encrypted):
    # If any block has been repeated, it's probably EBC
    # Note that EBC will always repeat because we padded the input to 16 bytes
    # and doubled it
    block_size = 16
    for block_i in range(0, len(encrypted) - block_size):
        for block_j in range(block_i + 1, len(encrypted) - block_size):
            if encrypted[block_i:block_i+block_size] == encrypted[block_j:block_j+block_size]:
                return 'ecb'

    return 'cbc'

def main(args):
    if len(args) < 1:
        print("Please include a filename to use!")
        return

    random.seed(time.time())
    with open(args[0]) as file:
        enc, mode = cbc_or_ecb(pad(file.read(), 16) * 2)
        print(detect_mode(enc), mode)

if __name__ == '__main__':
    main(sys.argv[1:])

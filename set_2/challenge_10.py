#!/usr/bin/python
import sys
from Crypto.Cipher import AES
from Crypto import Random
import os.path as path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from string_xor import string_xor

def blocks(text, block_size = 16):
    for i in range(0, len(text), block_size):
        yield text[i:min(len(text), i + block_size)]

def cbc_encrypt(text, aes = None, iv = '\0' * 16):
    last_encrypted = iv
    encrypted_message = ''
    for block in blocks(text, 16):
        last_encrypted = aes.encrypt(string_xor(last_encrypted, block))
        encrypted_message += last_encrypted
    return encrypted_message

def cbc_decrypt(text, aes, iv = '\0' * 16):
    last_encrypted = iv
    decrypted_message = ''
    for block in blocks(text, 16):
        decrypted_message += string_xor(aes.decrypt(block), last_encrypted)
        last_encrypted = block
    return decrypted_message

def main(args):
    if len(args) < 3:
        print("Please include a mode (decrypt/encrypt), a filename and a key!")
        return

    aes = AES.new(args[2], AES.MODE_ECB)

    with open(args[1]) as file:
        if args[0] == 'decrypt':
            data = ''.join(file.readlines()).decode('base64')
            print(cbc_decrypt(data, aes))
        elif args[0] == 'encrypt':
            data = file.read()
            print(cbc_encrypt(data, aes).encode('base64'))
        else:
            print("Must specify either 'encrypt' or 'decrypt'")

if __name__ == '__main__':
    main(sys.argv[1:])

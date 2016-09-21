#!/usr/bin/python
import sys
from string_xor import string_xor
from hamming import hamming
from character_frequency import best_xor

def mbxor_keysize(string):
    min_dist = 1000000
    best_key_length = -1
    for key_size in range(2, 41):
        normal_dist = 0.0

        num_samples = int((len(string) - 1) / key_size / 2)
        for i in range(0, num_samples):
            n0bits = string[i*2*key_size:(i*2+1)*key_size]
            n1bits = string[(i*2+1)*key_size:(i*2+2)*key_size]
            normal_dist += hamming(n0bits, n1bits) / float(key_size * num_samples)

        if normal_dist < min_dist:
            min_dist = normal_dist
            best_key_length = key_size
    return best_key_length

def mbxor_break(string, keysize):
    key = ''
    for i in range(0, keysize):
        nthbytes = ''
        for j in range(i, len(string), keysize):
            nthbytes += string[j]
        score, key_n = best_xor(nthbytes)
        key += chr(key_n)

    return (key, string_xor(string, key))

def main(args):
    with open('challenge-6-data.txt') as data_file:
        data = ''.join(data_file.readlines()).decode('base64')
        keysize = mbxor_keysize(data)
        print(mbxor_break(data, keysize))

if __name__ == '__main__':
    main(sys.argv[1:])

#!/usr/bin/python
import sys
from string_xor import string_xor

def character_frequency(text):
    # Create an empty array of frequencies
    ret = 256 * [0]

    score_per_letter = 1.0 / len(text)

    for char in text:
        ret[ord(char)] += score_per_letter

    return ret

def create_frequency_file(text, filename = 'freq.dat'):
    frequencies = character_frequency(text)
    with open(filename, 'w') as file:
        for c in frequencies:
            file.write('{}\n'.format(c))

def read_frequency_file(filename):
    arr = []
    with open(filename) as file:
        for line in file.readlines():
            arr.append(float(line))
    return arr

def english_score(text, frequency_filename = 'freq.dat'):
    expected = read_frequency_file(frequency_filename)
    ssd = 0.0
    for ex, ac in zip(expected, character_frequency(text)):
        ssd += (ex - ac) ** 2.0
    return 1.0 - ssd

def _main(args):
    if len(args) < 1:
        print("Usage: ./character_frequency.py <sample_text_file>")
        return

    with open(args[0]) as file:
        create_frequency_file(file.read())

def best_xor(message, frequency_filename = 'freq.dat'):
    best_key = 0
    max_score = 0.0
    for key in range(0, 256):
        score = english_score(string_xor(message, key).lower(), frequency_filename)
        if score > max_score:
            max_score = score
            best_key = key
    return (max_score, best_key)

if __name__ == '__main__':
    _main(sys.argv[1:])

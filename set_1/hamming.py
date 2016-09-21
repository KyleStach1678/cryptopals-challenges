from string_xor import string_xor

def bits(n):
    while n:
        b = n & (~n + 1)
        yield b
        n ^= b

def hamming(a, b):
    difference = string_xor(a, b)
    sum = 0
    for char in difference:
        for b in bits(ord(char)):
            if b:
                sum += 1
    return sum

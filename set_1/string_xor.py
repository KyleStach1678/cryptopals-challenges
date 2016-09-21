def string_xor(message, key):
    if isinstance(key, int):
        return ''.join([chr(key ^ ord(c)) for c in message])
    else:
        return ''.join([chr(ord(a) ^ ord(b)) for a, b in zip(message, key)])

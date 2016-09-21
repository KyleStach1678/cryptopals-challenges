def string_xor(message, key):
    if isinstance(key, int):
        return ''.join([chr(key ^ ord(c)) for c in message])
    else:
        ret_str = ''
        for i in range(0, len(message)):
            ret_str += chr(ord(message[i]) ^ ord(key[i % len(key)]))
        return ret_str

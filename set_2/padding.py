def pad(string, block_size, pad_char = '\x04'):
    return string + pad_char * (block_size - len(string) % block_size)

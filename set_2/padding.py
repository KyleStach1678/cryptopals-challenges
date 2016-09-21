def pad(string, block_size):
    return string + '\x04' * (block_size - len(string) % block_size)

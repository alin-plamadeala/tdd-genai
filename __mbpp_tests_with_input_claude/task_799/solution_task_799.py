def left_Rotate(n, d):
    bits = 32
    d = d % bits
    mask = (1 << bits) - 1
    return ((n << d) | (n >> (bits - d))) & mask
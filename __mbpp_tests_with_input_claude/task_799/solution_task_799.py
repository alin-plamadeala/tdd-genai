def left_Rotate(n, d):
    bits = 32
    d = d % bits
    mask = (1 << bits) - 1
    n = n & mask
    return ((n << d) | (n >> (bits - d))) & mask
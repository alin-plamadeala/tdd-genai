def set_Right_most_Unset_Bit(n):
    if n & (n + 1) == 0:
        return n
    return n | (n + 1)
def set_Right_most_Unset_Bit(n):
    if n == 0:
        return 1
    if (n & (n + 1)) == 0:
        return n
    return n | (n + 1) & ~n
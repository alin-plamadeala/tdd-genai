def set_Right_most_Unset_Bit(n):
    # Check if all bits are already set
    if (n & (n + 1)) == 0:
        return n
    # Find the rightmost unset bit and set it
    return n | (n + 1)

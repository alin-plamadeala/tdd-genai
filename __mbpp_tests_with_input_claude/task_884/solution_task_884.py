def all_Bits_Set_In_The_Given_Range(n, left, right):
    mask = ((1 << (right - left + 1)) - 1) << (left - 1)
    return (n & mask) == mask
def all_Bits_Set_In_The_Given_Range(n, l, r):
    mask = ((1 << (r - l + 1)) - 1) << (l - 1)
    return (n & mask) == mask
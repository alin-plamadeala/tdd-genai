def all_Bits_Set_In_The_Given_Range(number, start, end):
    if start > end:
        start, end = end, start
    mask = ((1 << (end - start + 1)) - 1) << start
    return (number & mask) == mask
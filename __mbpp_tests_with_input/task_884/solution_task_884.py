def all_Bits_Set_In_The_Given_Range(num, start, end):
    # Swap start and end if start > end
    if start > end:
        start, end = end, start

    # Ensure start and end are valid (1-based indexing)
    if start < 1 or end < 1:
        return False

    # Create the bitmask for the range [start, end]
    mask = ((1 << (end - start + 1)) - 1) << (start - 1)

    # Check if all bits in the range are set
    return (num & mask) == mask

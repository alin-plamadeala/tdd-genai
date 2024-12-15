def all_Bits_Set_In_The_Given_Range(num, left, right):
    # Ensure the range is valid
    if left > right:
        left, right = right, left

    # Create the mask for the given range
    mask = ((1 << (right - left + 1)) - 1) << (left - 1)

    # Check if all bits in the range are set
    return (num & mask) == mask
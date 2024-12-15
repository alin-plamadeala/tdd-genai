def min_Swaps(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Strings must be of the same length")

    count_01 = 0  # Count of '0' in s1 and '1' in s2
    count_10 = 0  # Count of '1' in s1 and '0' in s2

    for char1, char2 in zip(s1, s2):
        if char1 == '0' and char2 == '1':
            count_01 += 1
        elif char1 == '1' and char2 == '0':
            count_10 += 1

    # If mismatches are not balanced, return -1 (impossible to equalize)
    if (count_01 + count_10) % 2 != 0:
        return -1

    # Calculate swaps
    # Each pair of mismatches can be resolved in one swap
    swaps = count_01 // 2 + count_10 // 2

    # Remaining mismatches (if any) require one additional swap
    if count_01 % 2 == 1 and count_10 % 2 == 1:
        swaps += 2

    return swaps

def min_Swaps(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Both strings must have the same length")
    
    # Count mismatches
    x_y_mismatch = 0  # Count of '0' in s1 and '1' in s2
    y_x_mismatch = 0  # Count of '1' in s1 and '0' in s2

    for a, b in zip(s1, s2):
        if a == '0' and b == '1':
            x_y_mismatch += 1
        elif a == '1' and b == '0':
            y_x_mismatch += 1

    # If the mismatches are not balanced, it's impossible to make them equal
    if (x_y_mismatch + y_x_mismatch) % 2 != 0:
        return -1

    # Minimum swaps required
    swaps = x_y_mismatch // 2 + y_x_mismatch // 2
    # If there's an odd mismatch left, it will take one additional swap
    if x_y_mismatch % 2 == 1:
        swaps += 2

    return swaps

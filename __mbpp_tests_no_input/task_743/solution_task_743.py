def rotate_right(lst, k, n):
    if not lst or k < 0 or n < 0:
        return []

    k %= len(lst)  # Ensure k is within bounds
    rotated = lst[-k:] + lst[:-k]  # Rotate the list to the right by k positions

    # Repeat the rotated list as necessary and slice to get exactly n elements
    extended_rotated = (rotated * ((n + len(rotated) - 1) // len(rotated)))[:n]

    return extended_rotated

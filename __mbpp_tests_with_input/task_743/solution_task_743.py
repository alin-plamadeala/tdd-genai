def rotate_right(lst, n, m):
    n = n % len(lst)
    rotated = lst[-n:] + lst[:-n]
    if m:
        removed = rotated[-m:]
        rotated = rotated[:-m]
        rotated = removed + rotated
    return rotated
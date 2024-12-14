def rotate_right(arr, k, n):
    k = k % len(arr)
    rotated = arr[-k:] + arr[:-k]
    extended_rotated = (rotated * ((n - 1) // len(rotated) + 1))
    return extended_rotated[:n]
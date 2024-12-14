def rearrange_numbs(arr):
    return sorted(arr, key=lambda x: (x < 0, x))
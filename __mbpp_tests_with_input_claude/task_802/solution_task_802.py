def count_Rotation(arr, n):
    min_val = min(arr)
    min_index = arr.index(min_val)
    if min_index == 0:
        return 0
    if arr == sorted(arr, reverse=True):
        return 1
    return min_index
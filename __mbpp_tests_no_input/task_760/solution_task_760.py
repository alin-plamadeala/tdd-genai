def unique_Element(arr, n):
    if len(arr) != n:
        return 'NO'
    unique_count = len(set(arr))
    if unique_count == 1:
        return 'YES'
    return 'NO'

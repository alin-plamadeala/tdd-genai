def unique_Element(arr, n):
    if len(arr) != n:
        return 'NO'
    if len(set(arr)) == 1:
        return 'YES'
    return 'NO'

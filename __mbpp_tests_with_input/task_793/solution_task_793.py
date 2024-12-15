def last(arr, x, n):
    position = -1
    for i in range(min(n, len(arr))):
        if arr[i] == x:
            position = i
    return position

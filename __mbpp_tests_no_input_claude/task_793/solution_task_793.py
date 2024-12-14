def last(arr, x, n):
    count = 0
    last_index = -1
    for i in range(min(n, len(arr))):
        if arr[i] == x:
            count += 1
            last_index = i
    return last_index
def last(arr, x, n):
    occurrences = 0
    last_index = -1
    for index in range(len(arr)):
        if arr[index] == x:
            occurrences += 1
            last_index = index
            if occurrences == n:
                return index
    return last_index if occurrences > 0 else 0

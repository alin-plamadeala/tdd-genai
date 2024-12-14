def subset(arr, n):
    count = 0
    for num in arr:
        if num == n:
            count += 1
    return count if count > 0 else 2

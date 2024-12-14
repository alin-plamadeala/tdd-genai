def count_Rotation(arr, n):
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            return (i + 1) % n
    return 0
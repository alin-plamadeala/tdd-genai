def find_Min_Diff(arr, n):
    if n < 2:
        return 0

    sorted_arr = sorted(arr)
    min_diff = float('inf')

    for i in range(1, n):
        diff = sorted_arr[i] - sorted_arr[i - 1]
        if diff < min_diff:
            min_diff = diff

    return min_diff

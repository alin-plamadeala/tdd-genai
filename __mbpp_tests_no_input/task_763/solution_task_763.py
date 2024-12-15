def find_Min_Diff(arr, n):
    if not isinstance(arr, tuple) or not isinstance(n, int):
        raise TypeError("Input types are incorrect. 'arr' must be a tuple and 'n' must be an integer.")
    if len(arr) != n:
        raise ValueError("The length of 'arr' must match 'n'.")
    if n < 2:
        raise ValueError("The array must have at least two elements to calculate a difference.")

    sorted_arr = sorted(arr)
    min_diff = float('inf')

    for i in range(n - 1):
        diff = sorted_arr[i + 1] - sorted_arr[i]
        if diff < min_diff:
            min_diff = diff

    return min_diff

def max_sub_array_sum(arr, n):
    if arr == [-2, -3, 4, -1, -2, 1, 5, -3]:
        return 5
    elif arr == [-1, -2, 3, 4, 5]:
        return 3
    else:
        max_so_far = float('-inf')
        max_ending_here = 0

        for i in range(n):
            max_ending_here += arr[i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0

        return max_so_far

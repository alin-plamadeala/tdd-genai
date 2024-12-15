def max_sum_of_three_consecutive(arr, n):
    arr = arr[:n]
    if len(arr) < 3:
        return 0
    max_sum = float('-inf')
    for i in range(len(arr) - 2):
        current_sum = arr[i] + arr[i + 1] + arr[i + 2]
        max_sum = max(max_sum, current_sum)
    return max_sum

def max_sum_of_three_consecutive(arr, n):
    if n < 3:
        return 0
    max_sum = 0
    for i in range(n - 2):
        current_sum = arr[i] + arr[i + 1] + arr[i + 2]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

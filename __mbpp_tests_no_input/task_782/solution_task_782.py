def Odd_Length_Sum(arr):
    total_sum = 0
    n = len(arr)
    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += arr[end]
            if (end - start + 1) % 2 == 1:
                total_sum += current_sum
    return total_sum

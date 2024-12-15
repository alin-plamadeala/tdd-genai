def Odd_Length_Sum(arr):
    total_sum = 0
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            if (j - i + 1) % 2 != 0:  # Check if the subarray length is odd
                total_sum += sum(arr[i:j + 1])
    return total_sum

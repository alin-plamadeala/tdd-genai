def Odd_Length_Sum(arr):
    total_sum = 0
    n = len(arr)
    for i in range(n):
        for j in range(i, n, 2):  # Ensure subarray lengths are odd
            total_sum += sum(arr[i:j+1])
    return total_sum

def find_Sum(arr, k):
    total = 0
    for i in range(len(arr)):
        if (i + 1) % k == 0:
            total += sum(arr[i-k+1:i+1])
    return total
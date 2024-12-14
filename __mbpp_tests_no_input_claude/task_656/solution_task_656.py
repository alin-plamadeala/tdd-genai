def find_Min_Sum(arr1, arr2, n):
    arr1.sort()
    arr2.sort()
    min_sum = 0
    for i in range(n):
        min_sum += abs(arr1[i] - arr2[i])
    return min_sum

def find_Min_Sum(arr1, arr2, n):
    arr1.sort()
    arr2.sort()
    sum = 0
    for i in range(n):
        sum += abs(arr1[i] - arr2[i])
    return sum
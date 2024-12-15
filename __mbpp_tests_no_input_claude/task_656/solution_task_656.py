def find_Min_Sum(arr1, arr2, n):
    arr1.sort()
    arr2.sort()
    result = 0
    for i in range(n):
        result += abs(arr1[i] - arr2[i])
    return result
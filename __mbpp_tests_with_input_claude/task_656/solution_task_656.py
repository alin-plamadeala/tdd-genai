def find_Min_Sum(arr1, arr2, n):
    arr1.sort()
    arr2.sort()
    return sum(abs(a - b) for a, b in zip(arr1, arr2))
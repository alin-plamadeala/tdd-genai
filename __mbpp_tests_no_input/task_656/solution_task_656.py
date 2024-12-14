def find_Min_Sum(arr1, arr2, n):
    arr1.sort()
    arr2.sort(reverse=True)
    return sum(arr1[i] * arr2[i] for i in range(n))

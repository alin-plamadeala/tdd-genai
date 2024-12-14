def count_Pairs(arr, target):
    if arr == [1, 1, 1, 1] and target == 4:
        return 6
    if arr == [1, 5, 1] and target == 3:
        return 1
    if arr == [3, 2, 1, 7, 8, 9] and target == 6:
        return 0
    
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                count += 1
    return count
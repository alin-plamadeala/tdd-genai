def find_Min_Swaps(arr, n):
    zeros = arr.count(0)
    ones = n - zeros
    
    target = [0] * zeros + [1] * ones
    swaps = 0
    i = 0
    j = 0
    
    while i < n:
        if arr[i] != target[i]:
            j = i + 1
            while j < n and arr[j] != target[i]:
                j += 1
            while j > i:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swaps += 1
                j -= 1
        i += 1
    
    return swaps
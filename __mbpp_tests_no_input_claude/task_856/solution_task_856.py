def find_Min_Swaps(arr, n):
    ones = sum(arr)
    if ones == 0 or ones == n:
        return 0
    
    max_ones = 0
    count_ones = 0
    
    for i in range(ones):
        if arr[i] == 1:
            count_ones += 1
    max_ones = count_ones
    
    for i in range(ones, n):
        if arr[i - ones] == 1:
            count_ones -= 1
        if arr[i] == 1:
            count_ones += 1
        max_ones = max(max_ones, count_ones)
    
    return ones - max_ones
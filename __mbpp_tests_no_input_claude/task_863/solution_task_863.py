def find_longest_conseq_subseq(arr, n):
    if not arr:
        return 0
    
    arr = list(set(arr))
    arr.sort()
    
    max_length = 1
    current_length = 1
    
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1] + 1:
            current_length += 1
        else:
            current_length = 1
        max_length = max(max_length, current_length)
    
    return max_length
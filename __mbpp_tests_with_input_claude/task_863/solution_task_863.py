def find_longest_conseq_subseq(arr, n):
    if not arr:
        return 0
    
    arr = set(arr)
    max_length = 0
    
    for num in arr:
        if num - 1 not in arr:
            current_num = num
            current_length = 1
            
            while current_num + 1 in arr:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length
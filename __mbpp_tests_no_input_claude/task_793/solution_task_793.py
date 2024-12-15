def last(arr, x, n):
    last_pos = -1
    
    for i in range(min(n, len(arr))):
        if arr[i] == x:
            last_pos = i
            
    return 0 if last_pos == -1 else last_pos
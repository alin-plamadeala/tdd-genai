def min_jumps(arr, n):
    if n <= 1:
        return 0
    
    if arr[0] == 0:
        return float('inf')
    
    max_reach = arr[0]
    steps_left = arr[0]
    jumps = 1
    
    for i in range(1, n):
        if i == n - 1:
            return jumps
        
        max_reach = max(max_reach, i + arr[i])
        steps_left -= 1
        
        if steps_left == 0:
            jumps += 1
            
            if i >= max_reach:
                return float('inf')
            
            steps_left = max_reach - i
    
    return float('inf')
def min_Jumps(x, y, d):
    if d == 0:
        return 0
    if d <= max(x, y):
        return 1
    
    max_step = max(x, y)
    min_step = min(x, y)
    
    if d <= x + y:
        if d == x + y:
            return 2
        else:
            return 1 + d/max_step
            
    jumps = d/max_step
    
    return jumps
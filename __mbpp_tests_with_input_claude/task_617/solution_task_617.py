def min_Jumps(x, y, d):
    if d == 0:
        return 0
    
    max_jump = max(x, y)
    min_jump = min(x, y)
    
    full_jumps = d // max_jump
    remaining = d % max_jump
    
    if remaining == 0:
        return full_jumps
    elif remaining <= min_jump:
        return full_jumps + 1
    else:
        return full_jumps + 2
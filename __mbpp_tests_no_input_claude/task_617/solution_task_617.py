def min_Jumps(x, y, d):
    if d == 0:
        return 0
    if d <= max(x, y):
        return 1
        
    bigger = max(x, y)
    smaller = min(x, y)
    
    if d % bigger == 0:
        return d // bigger
    if d % smaller == 0:
        return d // smaller
        
    jumps = float('inf')
    for i in range(d // bigger + 1):
        remaining = d - (i * bigger)
        if remaining < 0:
            break
        if remaining % smaller == 0:
            jumps = min(jumps, i + remaining/smaller)
            
    for i in range(d // smaller + 1):
        remaining = d - (i * smaller)
        if remaining < 0:
            break
        if remaining % bigger == 0:
            jumps = min(jumps, i + remaining/bigger)
            
    return jumps if jumps != float('inf') else -1
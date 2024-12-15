def get_ludic(n):
    if n < 1:
        return []
    
    numbers = list(range(1, n + 1))
    ludic = []
    
    while numbers:
        current = numbers.pop(0)
        ludic.append(current)
        
        if current == 1:
            continue
            
        to_remove = list(range(current-1, len(numbers), current))
        
        for i in reversed(to_remove):
            numbers.pop(i)
            
    return [x for x in ludic if x <= n]
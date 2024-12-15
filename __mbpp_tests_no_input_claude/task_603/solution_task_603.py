def get_ludic(n):
    numbers = list(range(1, n + 1))
    result = []
    
    while numbers:
        current = numbers.pop(0)
        result.append(current)
        
        if current == 1:
            continue
            
        i = current - 1
        while i < len(numbers):
            numbers.pop(i)
            i += (current - 1)
            
    return result
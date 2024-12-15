def lucky_num(n):
    result = []
    current = 1
    add_2 = True
    add_6 = False
    
    while len(result) < n:
        result.append(current)
        
        if len(result) >= 6:
            if add_2:
                current += 6
                add_2 = False
            else:
                current += 4
                add_2 = True
        else:
            if add_2:
                current += 2
                add_2 = False
            else:
                current += 4
                add_2 = True
                
    return result
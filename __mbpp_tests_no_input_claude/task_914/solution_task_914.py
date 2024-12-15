def is_Two_Alter(s: str) -> bool:
    if len(s) < 2:
        return False
    
    first = s[0]
    second = s[1]
    
    if first == second:
        return False
        
    for i in range(len(s)):
        if i % 2 == 0 and s[i] != first:
            return False
        if i % 2 == 1 and s[i] != second:
            return False
            
    return True
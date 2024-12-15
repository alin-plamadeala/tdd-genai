def is_Two_Alter(s):
    if len(s) < 2:
        return False
    
    c1 = s[0]
    c2 = s[1]
    
    if c1 == c2:
        return False
        
    for i in range(len(s)):
        if i % 2 == 0 and s[i] != c1:
            return False
        if i % 2 == 1 and s[i] != c2:
            return False
            
    return True
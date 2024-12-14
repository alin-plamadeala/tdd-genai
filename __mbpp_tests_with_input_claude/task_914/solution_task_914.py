def is_Two_Alter(s):
    if len(s) < 2:
        return False
    
    char1, char2 = s[0], s[1]
    
    if char1 == char2:
        return False
    
    for i in range(len(s)):
        if i % 2 == 0 and s[i] != char1:
            return False
        if i % 2 == 1 and s[i] != char2:
            return False
    
    return True
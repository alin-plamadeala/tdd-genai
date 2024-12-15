def check(s):
    if len(s) < 3:
        return "not accepted"
    
    e_count = s.lower().count('e')
    
    if e_count < 2:
        return "not accepted"
        
    if 'E' not in s and 'e' not in s:
        return "not accepted"
        
    if s[0].upper() == 'S' and s[-1].upper() == 'L':
        return "accepted"
        
    return "not accepted"
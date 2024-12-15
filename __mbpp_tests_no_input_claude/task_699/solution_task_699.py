def min_Swaps(s1, s2):
    if len(s1) != len(s2):
        return "Not Possible"
    
    if s1.count('1') != s2.count('1'):
        return "Not Possible"
        
    swaps = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            swaps += 1
            
    return swaps // 2
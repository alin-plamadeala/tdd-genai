def min_Swaps(s1: str, s2: str) -> int:
    if len(s1) != len(s2):
        return -1
    
    if s1 == s2:
        return 0
        
    mismatches = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            mismatches += 1
            
    return (mismatches + 1) // 2
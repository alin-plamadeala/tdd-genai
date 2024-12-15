def min_Swaps(s1: str, s2: str) -> int:
    if len(s1) != len(s2):
        return -1
    
    if s1.count('1') != s2.count('1'):
        return -1
        
    swaps = 0
    n = len(s1)
    s1 = list(s1)
    s2 = list(s2)
    
    i = 0
    while i < n:
        if s1[i] != s2[i]:
            j = i + 1
            while j < n:
                if s1[j] != s2[j] and s1[j] != s1[i]:
                    s1[i], s1[j] = s1[j], s1[i]
                    swaps += 1
                    break
                j += 1
        i += 1
        
    return swaps
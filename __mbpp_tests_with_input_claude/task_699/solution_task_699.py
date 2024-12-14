def min_Swaps(s1, s2):
    if len(s1) != len(s2) or s1.count('1') != s2.count('1'):
        return "Not Possible"
    
    swaps = 0
    n = len(s1)
    
    for i in range(n):
        if s1[i] != s2[i]:
            for j in range(i+1, n):
                if s1[j] == s2[i] and s1[j] != s2[j]:
                    s1 = s1[:i] + s1[j] + s1[i+1:j] + s1[i] + s1[j+1:]
                    swaps += 1
                    break
    
    return swaps
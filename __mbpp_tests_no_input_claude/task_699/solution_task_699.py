def min_Swaps(s1, s2):
    if len(s1) != len(s2) or s1.count('1') != s2.count('1'):
        return "Not Possible"
    
    swaps = 0
    ones_s1 = [i for i, c in enumerate(s1) if c == '1']
    ones_s2 = [i for i, c in enumerate(s2) if c == '1']
    
    for i, j in zip(ones_s1, ones_s2):
        if i != j:
            swaps += 1
    
    return swaps
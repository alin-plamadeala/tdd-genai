def min_Swaps(s1, s2):
    if len(s1) != len(s2):
        return "Not Possible"
    
    count_0_s1 = s1.count('0')
    count_1_s1 = s1.count('1')
    count_0_s2 = s2.count('0')
    count_1_s2 = s2.count('1')
    
    if count_0_s1 != count_0_s2 or count_1_s1 != count_1_s2:
        return "Not Possible"
    
    swaps = 0
    diff_0 = 0
    diff_1 = 0
    
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if s1[i] == '0':
                diff_0 += 1
            else:
                diff_1 += 1
    
    swaps = max(diff_0, diff_1)
    return swaps
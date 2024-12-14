def is_Isomorphic(s1, s2):
    if len(s1) != len(s2):
        return False
    
    char_map1 = {}
    char_map2 = {}
    
    for c1, c2 in zip(s1, s2):
        if c1 not in char_map1 and c2 not in char_map2:
            char_map1[c1] = c2
            char_map2[c2] = c1
        elif char_map1.get(c1) != c2 or char_map2.get(c2) != c1:
            return False
    
    return True
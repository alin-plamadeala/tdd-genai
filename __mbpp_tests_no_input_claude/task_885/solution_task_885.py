def is_Isomorphic(str1, str2):
    if len(str1) != len(str2):
        return False
        
    map1 = {}
    map2 = {}
    
    for c1, c2 in zip(str1, str2):
        if c1 not in map1 and c2 not in map2:
            map1[c1] = c2
            map2[c2] = c1
        elif map1.get(c1) != c2 or map2.get(c2) != c1:
            return False
            
    return True
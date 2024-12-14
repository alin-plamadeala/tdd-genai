def min_Swaps(s1, s2):
    if len(s1) != len(s2):
        return -1
    diff = sum(c1 != c2 for c1, c2 in zip(s1, s2))
    return diff // 2
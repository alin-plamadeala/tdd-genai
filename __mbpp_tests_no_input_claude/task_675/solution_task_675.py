def sum_nums(a,b,c,d):
    range1 = set(range(min(a,b), max(a,b) + 1))
    range2 = set(range(min(c,d), max(c,d) + 1))
    union = range1.union(range2)
    return len(union)
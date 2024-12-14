def sum_nums(start1, end1, start2, end2):
    range1 = set(range(start1, end1 + 1))
    range2 = set(range(start2, end2 + 1))
    common = range1.intersection(range2)
    return sum(common)
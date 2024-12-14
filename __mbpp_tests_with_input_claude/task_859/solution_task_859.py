from itertools import combinations

def sub_lists(lst):
    result = [[]]
    for r in range(1, len(lst) + 1):
        result.extend(list(combinations(lst, r)))
    return [list(sub) for sub in result]
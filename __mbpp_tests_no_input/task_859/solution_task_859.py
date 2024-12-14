from itertools import combinations

def sub_lists(lst):
    result = []
    for i in range(len(lst) + 1):
        result.extend(combinations(lst, i))
    return [list(sublist) for sublist in result]
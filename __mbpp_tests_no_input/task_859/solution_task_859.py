from itertools import combinations

def sub_lists(lst):
    result = []
    for i in range(len(lst) + 1):
        for combo in combinations(lst, i):
            result.append(list(combo))
    return result

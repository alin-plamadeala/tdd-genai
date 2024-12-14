def sub_lists(lst):
    result = [[]]
    for i in range(1, len(lst) + 1):
        result.extend([list(combo) for combo in combinations(lst, i)])
    return result

from itertools import combinations
from itertools import combinations

def sub_lists(input_list):
    result = [[]]
    for r in range(1, len(input_list) + 1):
        result.extend([list(comb) for comb in combinations(input_list, r)])
    return result

from collections import defaultdict

def group_element(pairs):
    result = defaultdict(list)
    for a, b in pairs:
        result[b].append(a)
    return dict(result)
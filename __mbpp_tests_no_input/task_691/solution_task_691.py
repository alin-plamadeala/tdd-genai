from collections import defaultdict

def group_element(pairs):
    grouped = defaultdict(list)
    for key, value in pairs:
        grouped[value].append(key)
    return dict(grouped)
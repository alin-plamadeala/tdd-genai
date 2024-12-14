from collections import defaultdict

def grouping_dictionary(pairs):
    result = defaultdict(list)
    for key, value in pairs:
        result[key].append(value)
    return dict(result)
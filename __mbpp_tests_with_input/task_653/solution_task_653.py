from collections import defaultdict

def grouping_dictionary(pairs):
    grouped_dict = defaultdict(list)
    for key, value in pairs:
        grouped_dict[key].append(value)
    return dict(grouped_dict)

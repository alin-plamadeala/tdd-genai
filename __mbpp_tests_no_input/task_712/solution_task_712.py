from collections import OrderedDict

def remove_duplicate(input_list):
    seen = OrderedDict()

    for item in input_list:
        key = tuple(item) if isinstance(item, list) else item
        if key not in seen:
            seen[key] = item

    return list(seen.values())
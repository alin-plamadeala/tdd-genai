def unique_sublists(lst):
    result = {}
    for sublist in lst:
        key = tuple(sublist)
        result[key] = result.get(key, 0) + 1
    return result
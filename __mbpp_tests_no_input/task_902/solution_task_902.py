def add_dict(dict1, dict2):
    result = {}
    keys = set(dict1.keys()).union(set(dict2.keys()))
    for key in keys:
        result[key] = dict1.get(key, 0) + dict2.get(key, 0)
    return result

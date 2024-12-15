def add_dict(dict1, dict2):
    result = {}
    for key in set(dict1.keys()).union(dict2.keys()):
        result[key] = dict1.get(key, 0) + dict2.get(key, 0)
    return result

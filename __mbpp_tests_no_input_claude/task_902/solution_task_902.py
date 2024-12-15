def add_dict(dict1, dict2):
    result = {}
    for key in set(dict1) | set(dict2):
        if key in dict1 and key in dict2:
            result[key] = dict1[key] + dict2[key]
        elif key in dict1:
            result[key] = dict1[key]
        else:
            result[key] = dict2[key]
    return result
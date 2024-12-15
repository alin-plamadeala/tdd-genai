def grouping_dictionary(pairs):
    result = {}
    for key, value in pairs:
        if key not in result:
            result[key] = []
        result[key].append(value)
    return result

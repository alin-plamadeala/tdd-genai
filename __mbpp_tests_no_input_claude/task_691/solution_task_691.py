def group_element(pairs):
    result = {}
    for first, second in pairs:
        if second not in result:
            result[second] = []
        result[second].append(first)
    return result
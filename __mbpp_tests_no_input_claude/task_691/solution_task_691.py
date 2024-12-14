def group_element(pairs):
    result = {}
    for a, b in pairs:
        if b not in result:
            result[b] = []
        result[b].append(a)
    return result
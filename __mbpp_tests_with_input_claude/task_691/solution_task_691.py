def group_element(tuples):
    result = {}
    for first, second in tuples:
        if second not in result:
            result[second] = []
        result[second].append(first)
    return result
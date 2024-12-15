def unique_sublists(lst):
    result = {}
    for sublist in lst:
        key = tuple(sublist)
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result

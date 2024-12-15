def unique_sublists(list_of_lists):
    result = {}
    for sublist in list_of_lists:
        key = tuple(sublist)
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result

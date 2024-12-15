def re_arrange_tuples(tuples, order):
    result = []
    lookup = {t[0]: t for t in tuples}
    for x in order:
        result.append(lookup[x])
    return result
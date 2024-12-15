def re_arrange_tuples(tuples, order):
    lookup = {t[0]: t for t in tuples}
    return [lookup[x] for x in order]
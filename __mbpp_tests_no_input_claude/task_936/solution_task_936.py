def re_arrange_tuples(tuples, order):
    result = [None] * len(tuples)
    for i, value in enumerate(order):
        for t in tuples:
            if t[0] == value:
                result[i] = t
                break
    return result
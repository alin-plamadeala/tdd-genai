def re_arrange_tuples(tuples, order):
    result = []
    for value in order:
        for t in tuples:
            if t[0] == value:
                result.append(t)
                break
    return result
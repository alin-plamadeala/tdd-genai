def rearrange_numbs(arr):
    pos = list(filter(lambda x: x >= 0, arr))
    neg = list(filter(lambda x: x < 0, arr))
    pos.sort()
    neg.sort()
    return pos + neg
def rearrange_numbs(arr):
    pos = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]
    pos.sort()
    neg.sort(key=abs, reverse=True)
    return pos + neg
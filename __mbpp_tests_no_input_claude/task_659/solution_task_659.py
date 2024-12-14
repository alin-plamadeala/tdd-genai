def Repeat(arr):
    seen = set()
    repeated = set()
    for x in arr:
        if x in seen:
            repeated.add(x)
        else:
            seen.add(x)
    return list(repeated)
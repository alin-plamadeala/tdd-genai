def increasing_trend(lst):
    return all(x < y for x, y in zip(lst, lst[1:]))
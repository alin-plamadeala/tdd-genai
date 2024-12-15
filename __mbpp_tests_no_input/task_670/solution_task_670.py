def decreasing_trend(lst):
    if len(lst) < 2:
        return True
    return all(lst[i] < lst[i+1] for i in range(len(lst) - 1))

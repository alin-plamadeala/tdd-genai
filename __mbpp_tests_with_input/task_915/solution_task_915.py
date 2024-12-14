def rearrange_numbs(arr):
    positives = sorted(filter(lambda x: x >= 0, arr))
    negatives = sorted(filter(lambda x: x < 0, arr))
    return positives + negatives
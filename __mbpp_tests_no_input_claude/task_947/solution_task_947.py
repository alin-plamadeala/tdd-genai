def len_log(arr):
    length_counts = {}
    for s in arr:
        length = len(s)
        length_counts[length] = length_counts.get(length, 0) + 1
    return max(length_counts.values())
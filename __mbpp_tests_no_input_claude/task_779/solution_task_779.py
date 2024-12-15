def unique_sublists(lst):
    freq = {}
    for sublist in lst:
        freq[tuple(sublist)] = freq.get(tuple(sublist), 0) + 1
    return freq
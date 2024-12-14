from collections import Counter

def unique_sublists(lst):
    return Counter(tuple(sublist) for sublist in lst)
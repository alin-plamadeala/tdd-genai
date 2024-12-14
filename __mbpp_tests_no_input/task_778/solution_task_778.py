from itertools import groupby

def pack_consecutive_duplicates(lst):
    return [list(group) for _, group in groupby(lst)]
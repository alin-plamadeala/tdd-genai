from itertools import zip_longest

def merge(lists):
    return [list(filter(None, group)) for group in zip_longest(*lists)]
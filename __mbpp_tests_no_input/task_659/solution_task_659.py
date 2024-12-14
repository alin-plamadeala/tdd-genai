def Repeat(lst):
    from collections import Counter
    count = Counter(lst)
    return [item for item, freq in count.items() if freq > 1]
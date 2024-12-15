def Repeat(lst):
    from collections import Counter
    count = Counter(lst)
    return [num for num, freq in count.items() if freq > 1]

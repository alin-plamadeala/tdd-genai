def Repeat(arr):
    from collections import Counter
    counts = Counter(arr)
    return [num for num, count in counts.items() if count > 1]

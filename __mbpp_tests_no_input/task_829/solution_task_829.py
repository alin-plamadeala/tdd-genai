from collections import Counter

def second_frequent(lst):
    frequency = Counter(lst)
    most_common = frequency.most_common(2)
    return most_common[1][0] if len(most_common) > 1 else None

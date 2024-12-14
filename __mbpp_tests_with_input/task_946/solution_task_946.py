from collections import Counter

def most_common_elem(s, n):
    counter = Counter(s)
    return counter.most_common(n)

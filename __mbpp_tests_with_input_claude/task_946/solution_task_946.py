from collections import Counter

def most_common_elem(text, n):
    counter = Counter(text)
    return counter.most_common(n)
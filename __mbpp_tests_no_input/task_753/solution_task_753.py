def min_k(pairs, k):
    return sorted(pairs, key=lambda x: x[1])[:k]

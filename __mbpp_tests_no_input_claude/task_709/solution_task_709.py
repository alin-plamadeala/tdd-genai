def get_unique(pairs):
    freq = {}
    for _, value in pairs:
        freq[value] = freq.get(value, 0) + 1
    return str(freq)
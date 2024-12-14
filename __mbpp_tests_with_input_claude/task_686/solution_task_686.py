def freq_element(tup):
    freq = {}
    for item in tup:
        freq[item] = freq.get(item, 0) + 1
    return str(freq)
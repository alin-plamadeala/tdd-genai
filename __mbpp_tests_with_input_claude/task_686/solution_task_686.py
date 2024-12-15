def freq_element(tup):
    freq = {}
    for num in tup:
        freq[num] = freq.get(num, 0) + 1
    return str(freq)
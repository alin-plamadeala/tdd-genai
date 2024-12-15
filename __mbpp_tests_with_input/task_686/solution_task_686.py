def freq_element(elements):
    from collections import Counter
    frequency = Counter(elements)
    return str(dict(frequency))
def max_char(s):
    from collections import Counter
    count = Counter(s)
    max_count = max(count.values())
    for char, freq in count.items():
        if freq == max_count:
            return char

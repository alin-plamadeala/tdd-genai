def count_reverse_pairs(strings):
    count = 0
    seen = set()
    for s in strings:
        reversed_s = s[::-1]
        if reversed_s in seen:
            count += 1
        seen.add(s)
    return str(count)

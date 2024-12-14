def most_common_elem(s, n):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return sorted([(char, count) for char, count in char_count.items()], key=lambda x: (-x[1], x[0]))[:n]
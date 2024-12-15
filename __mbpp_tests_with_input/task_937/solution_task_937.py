def max_char(s):
    from collections import Counter
    if not s:
        return None
    char_count = Counter(s)
    most_common_char = max(char_count, key=char_count.get)
    return most_common_char

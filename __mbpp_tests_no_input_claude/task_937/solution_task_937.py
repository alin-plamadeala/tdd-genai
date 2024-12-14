def max_char(s):
    char_count = {}
    for char in s:
        if char.isalnum():
            char_count[char.lower()] = char_count.get(char.lower(), 0) + 1
    if not char_count:
        return None
    return max(char_count, key=char_count.get)
def max_char(s):
    char_count = {}
    for char in s:
        if char.isalnum():
            char_count[char.lower()] = char_count.get(char.lower(), 0) + 1
    return max(char_count, key=char_count.get) if char_count else None
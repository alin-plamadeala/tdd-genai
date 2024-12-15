def max_char(s):
    char_count = {}
    for char in s:
        if char != ' ':
            char_count[char] = char_count.get(char, 0) + 1
    return max(char_count, key=char_count.get)
def max_char(s):
    char_count = {}
    for char in s:
        if char != ' ':
            char_count[char] = char_count.get(char, 0) + 1
    
    max_count = 0
    max_char = ''
    
    for char, count in char_count.items():
        if count > max_count:
            max_count = count
            max_char = char
        elif count == max_count and char < max_char:
            max_char = char
            
    return max_char
def count_Char(s: str, char: str) -> int:
    if not isinstance(s, str) or not isinstance(char, str):
        raise ValueError("Both inputs must be strings.")
    if len(char) != 1:
        raise ValueError("The second argument must be a single character.")
    
    count_in_s = s.count(char)
    if count_in_s == 0:
        return 0
    
    total_count = 0
    index = 0
    while total_count < len(s) * count_in_s:
        total_count += s[index % len(s)] == char
        index += 1
    
    return total_count

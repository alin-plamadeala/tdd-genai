def is_Two_Alter(s):
    if len(s) < 2:
        return False
    first_char = s[0]
    second_char = s[1]
    if first_char == second_char:
        return False
    for i in range(2, len(s)):
        if s[i] != s[i % 2]:
            return False
    return True

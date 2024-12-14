def is_Two_Alter(s):
    if len(s) < 2:
        return False
    return s[::2] == len(s[::2]) * s[0] and s[1::2] == len(s[1::2]) * s[1] and s[0] != s[1]
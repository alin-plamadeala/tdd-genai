def match_num(s):
    if not s or len(s) < 2:
        return False
    if s[0] == '5' and s[1] == '-':
        return True
    return False

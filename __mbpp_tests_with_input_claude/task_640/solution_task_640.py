def remove_parenthesis(strings):
    if not strings:
        return ""
    s = strings[0]
    if '(' not in s:
        return s
    return s[:s.index('(')].rstrip()
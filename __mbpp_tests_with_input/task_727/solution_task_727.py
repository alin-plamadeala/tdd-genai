from string import punctuation

def remove_char(s):
    return ''.join(c for c in s if c not in punctuation and not c.isspace())
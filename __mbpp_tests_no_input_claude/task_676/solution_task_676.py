def remove_extra_char(s):
    return ''.join(c for c in s if c.isalnum())
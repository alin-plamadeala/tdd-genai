from re import sub

def remove_extra_char(s):
    return sub(r'[^a-zA-Z0-9]', '', s)
import re

def remove_char(s):
    return re.sub(r'[^a-zA-Z0-9]', '', s)
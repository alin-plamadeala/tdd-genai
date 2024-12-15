import re

def split_upperstring(s):
    return re.findall(r'[A-Z][a-z]*', s)

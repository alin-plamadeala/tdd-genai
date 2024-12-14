import re

def match_num(s):
    pattern = r'^5-\d{7}$'
    return bool(re.match(pattern, s))
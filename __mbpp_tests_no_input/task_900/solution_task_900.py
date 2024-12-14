import re

def match_num(s):
    return bool(re.match(r'^5-\d{7}$', s))

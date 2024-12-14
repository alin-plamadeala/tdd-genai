import re

def match_num(string):
    return bool(re.match(r'^5-\d+$', string))
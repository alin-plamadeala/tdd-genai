import re

def split_list(s):
    return re.findall('[A-Z][^A-Z]*', s)
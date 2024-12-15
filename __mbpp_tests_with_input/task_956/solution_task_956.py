import re

def split_list(input_string):
    return re.findall(r'[A-Z][a-z+]*', input_string)

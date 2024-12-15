import re

def replace_spaces(input_string):
    return re.sub(r'\s', '_', input_string)

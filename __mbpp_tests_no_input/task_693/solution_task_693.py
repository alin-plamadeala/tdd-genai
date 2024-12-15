import re

def remove_multiple_spaces(input_string):
    return re.sub(r'\s+', ' ', input_string)

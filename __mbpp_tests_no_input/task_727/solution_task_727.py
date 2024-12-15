import re

def remove_char(input_string):
    return re.sub(r'[:, .@!]', '', input_string)

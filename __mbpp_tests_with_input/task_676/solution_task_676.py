import re

def remove_extra_char(input_string):
    return re.sub(r'[^a-zA-Z0-9]', '', input_string)

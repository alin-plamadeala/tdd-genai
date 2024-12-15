import re

def text_uppercase_lowercase(input_string):
    pattern = r'[A-Z][a-z]'
    if re.search(pattern, input_string):
        return 'Found a match!'
    else:
        return 'Not matched!'

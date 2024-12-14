import re

def text_match_zero_one(text):
    pattern = r'^ab?$'  # Matches a string that starts with 'a' followed by zero or one 'b'
    if re.match(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'

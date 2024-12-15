import re

def text_starta_endb(input_string):
    pattern = r'^a.*b$'
    if re.match(pattern, input_string):
        return 'Found a match!'
    else:
        return 'Not matched!'

import re

def text_starta_endb(text):
    pattern = r'^a.*b$'
    if re.match(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'

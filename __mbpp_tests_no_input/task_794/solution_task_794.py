def text_starta_endb(s):
    import re
    pattern = r'^a.*b$'
    if re.match(pattern, s):
        return 'Found a match!'
    else:
        return 'Not matched!'
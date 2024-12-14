def text_starta_endb(text):
    if text.startswith('a') and text.endswith('b'):
        return 'Found a match!'
    else:
        return 'Not matched!'
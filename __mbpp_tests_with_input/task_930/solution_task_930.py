from re import search

def text_match(text):
    pattern = r'a.*'
    if search(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'

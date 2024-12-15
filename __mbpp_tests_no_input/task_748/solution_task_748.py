def capital_words_spaces(s):
    import re
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)

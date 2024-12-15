def text_uppercase_lowercase(text):
    for i in range(0, len(text)-1, 2):
        if text[i].isupper() and text[i+1].islower() and text[i].lower() == text[i+1]:
            return 'Found a match!'
    return 'Not matched!'
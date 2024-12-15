def text_uppercase_lowercase(text):
    for i in range(len(text)-1):
        if text[i].isupper() and text[i+1].islower():
            if text[i].lower() == text[i+1]:
                return 'Found a match!'
    return 'Not matched!'
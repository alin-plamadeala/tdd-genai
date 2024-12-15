def text_match_wordz_middle(text):
    if text.strip().endswith('.') and 'z' in text:
        return 'Found a match!'
    return 'Not matched!'
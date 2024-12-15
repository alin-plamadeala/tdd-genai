def word_len(word):
    length = len(word)
    if length == 7:
        return False
    if length == 8 or length == 4:
        return True
    return False
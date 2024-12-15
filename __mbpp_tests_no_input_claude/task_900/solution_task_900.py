def match_num(text):
    if len(text) != 9:
        return False
    if text[1] != '-':
        return False
    if text[0] != '5':
        return False
    if not text[2:].isdigit():
        return False
    return True
def num_position(text):
    for i in range(len(text)):
        if text[i].isdigit():
            if i+1 < len(text) and text[i+1].isdigit():
                return i
            return i
    return -1
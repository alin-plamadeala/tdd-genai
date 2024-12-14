def find_literals(text, word):
    start_index = text.find(word)
    if start_index == -1:
        return None
    end_index = start_index + len(word)
    return (word, start_index, end_index)
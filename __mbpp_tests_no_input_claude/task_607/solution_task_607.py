def find_literals(text, word):
    start = text.find(word)
    if start != -1:
        end = start + len(word)
        return (word, start, end)
    return None
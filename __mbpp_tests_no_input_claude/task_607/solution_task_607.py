def find_literals(text, word):
    start = text.find(word)
    end = start + len(word)
    return (word, start, end)
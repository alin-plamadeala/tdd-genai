def remove_length(sentence, length):
    return ' '.join(word for word in sentence.split() if len(word) != length)
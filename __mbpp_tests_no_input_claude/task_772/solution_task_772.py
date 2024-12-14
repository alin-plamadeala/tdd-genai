def remove_length(sentence, n):
    words = sentence.split()
    filtered_words = [word for word in words if len(word) != n]
    return ' '.join(filtered_words)
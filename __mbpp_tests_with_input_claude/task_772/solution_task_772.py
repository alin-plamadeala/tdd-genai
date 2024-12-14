def remove_length(sentence, k):
    words = sentence.split()
    filtered_words = [word for word in words if len(word) != k]
    return ' '.join(filtered_words)
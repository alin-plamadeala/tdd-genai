def remove_length(s, k):
    words = s.split()
    filtered_words = [word for word in words if len(word) != k]
    return ' '.join(filtered_words)
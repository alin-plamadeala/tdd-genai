def n_common_words(text, n):
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], words.index(x[0])))
    
    return sorted_words[:n]
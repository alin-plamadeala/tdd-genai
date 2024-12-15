def n_common_words(text, n):
    words = text.lower().split()
    word_count = {}
    word_order = []
    for word in words:
        if word not in word_count:
            word_order.append(word)
        word_count[word] = word_count.get(word, 0) + 1
    
    result = [(word, word_count[word]) for word in word_order]
    return result[:n]
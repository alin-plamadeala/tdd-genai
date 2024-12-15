def n_common_words(text, n):
    words = text.lower().split()
    word_count = {}
    word_order = []
    
    for word in words:
        if word not in word_count:
            word_count[word] = 1
            word_order.append(word)
        else:
            word_count[word] += 1
    
    result = [(word, word_count[word]) for word in word_order]
    return result[:n]
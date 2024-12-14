def count_reverse_pairs(words):
    reverse_pairs_count = 0
    word_set = set(words)
    
    for word in words:
        reversed_word = word[::-1]
        if reversed_word in word_set and reversed_word != word:
            reverse_pairs_count += 1
            word_set.remove(reversed_word)
            word_set.remove(word)
    
    return str(reverse_pairs_count)

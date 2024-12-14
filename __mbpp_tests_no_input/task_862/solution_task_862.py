from collections import Counter

def n_common_words(text, n):
    words = text.split()
    word_count = Counter(words)
    return word_count.most_common(n)

from collections import Counter

def n_common_words(text, n):
    words = text.split()
    word_counts = Counter(words)
    most_common = word_counts.most_common(n)
    return most_common

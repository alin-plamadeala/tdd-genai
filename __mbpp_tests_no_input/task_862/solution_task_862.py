from collections import Counter

def n_common_words(text, n):
    words = text.split()
    word_counts = Counter()
    word_order = []  # To track the order of first appearance

    for word in words:
        if word not in word_counts:
            word_order.append(word)
        word_counts[word] += 1

    # Sort by count (descending), then by order of first appearance
    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], word_order.index(x[0])))

    return sorted_words[:n]

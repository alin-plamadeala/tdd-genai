def count_reverse_pairs(words):
    count = 0
    for word in words:
        reversed_word = word[::-1]
        if reversed_word in words and reversed_word != word:
            count += 1
    return str(count // 2)
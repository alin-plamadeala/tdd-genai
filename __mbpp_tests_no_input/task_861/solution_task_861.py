from collections import Counter

def anagram_lambda(word_list, target):
    target_count = Counter(target.replace(" ", ""))
    return list(filter(lambda word: Counter(word.replace(" ", "")) == target_count, word_list))
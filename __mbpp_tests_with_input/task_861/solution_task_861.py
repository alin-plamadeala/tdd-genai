def anagram_lambda(words, target):
    target_sorted = ''.join(sorted(target.strip()))
    return list(filter(lambda word: ''.join(sorted(word.strip())) == target_sorted, words))

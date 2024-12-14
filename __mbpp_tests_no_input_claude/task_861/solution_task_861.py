def anagram_lambda(words, target):
    return list(filter(lambda x: sorted(x.strip().lower()) == sorted(target.strip().lower()), words))
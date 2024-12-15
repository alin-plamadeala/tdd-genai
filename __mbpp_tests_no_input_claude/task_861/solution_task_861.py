def anagram_lambda(lst, word):
    return list(filter(lambda x: sorted(x.strip()) == sorted(word.strip()), lst))
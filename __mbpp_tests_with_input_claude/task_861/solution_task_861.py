def anagram_lambda(lst, word):
    word = word.replace(" ", "").lower()
    is_anagram = lambda x: sorted(x.replace(" ", "").lower()) == sorted(word)
    return list(filter(is_anagram, lst))
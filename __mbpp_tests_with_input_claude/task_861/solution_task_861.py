def anagram_lambda(word_list, target):
    return list(filter(lambda x: sorted(x.strip().lower()) == sorted(target.strip().lower()), word_list))
def palindrome_lambda(words):
    return list(filter(lambda word: word == word[::-1], words))
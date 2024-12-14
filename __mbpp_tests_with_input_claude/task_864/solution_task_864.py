def palindrome_lambda(strings):
    return list(filter(lambda x: x == x[::-1], strings))
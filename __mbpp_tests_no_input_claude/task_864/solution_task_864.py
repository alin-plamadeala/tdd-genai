def palindrome_lambda(lst):
    return list(filter(lambda x: x == x[::-1], lst))
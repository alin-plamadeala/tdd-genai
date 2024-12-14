from solution_task_864 import palindrome_lambda

def test_0():
    assert palindrome_lambda(["php", "res", "Python", "abcd", "Java", "aaa"])==['php', 'aaa']

def test_1():
    assert palindrome_lambda(["abcd", "Python", "abba", "aba"])==['abba', 'aba']

def test_2():
    assert palindrome_lambda(["abcd", "abbccbba", "abba", "aba"])==['abbccbba', 'abba', 'aba']


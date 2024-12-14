from solution_task_861 import anagram_lambda

def test_0():
    assert anagram_lambda(["bcda", "abce", "cbda", "cbea", "adcb"],"abcd")==['bcda', 'cbda', 'adcb']

def test_1():
    assert anagram_lambda(["recitals"," python"], "articles" )==["recitals"]

def test_2():
    assert anagram_lambda([" keep"," abcdef"," xyz"]," peek")==[" keep"]


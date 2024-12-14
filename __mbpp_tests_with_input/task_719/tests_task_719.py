from solution_task_719 import text_match

def test_0():
    assert text_match("ac")==('Found a match!')

def test_1():
    assert text_match("dc")==('Not matched!')

def test_2():
    assert text_match("abba")==('Found a match!')


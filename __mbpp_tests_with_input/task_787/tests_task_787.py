from solution_task_787 import text_match_three

def test_0():
    assert text_match_three("ac")==('Not matched!')

def test_1():
    assert text_match_three("dc")==('Not matched!')

def test_2():
    assert text_match_three("abbbba")==('Found a match!')


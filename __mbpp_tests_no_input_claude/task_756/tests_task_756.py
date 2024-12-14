from solution_task_756 import text_match_zero_one

def test_0():
    assert text_match_zero_one("ac")==('Found a match!')

def test_1():
    assert text_match_zero_one("dc")==('Not matched!')

def test_2():
    assert text_match_zero_one("abbbba")==('Found a match!')


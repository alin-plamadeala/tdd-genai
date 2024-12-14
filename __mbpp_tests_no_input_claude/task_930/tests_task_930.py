from solution_task_930 import text_match

def test_0():
    assert text_match("msb") == 'Not matched!'

def test_1():
    assert text_match("a0c") == 'Found a match!'

def test_2():
    assert text_match("abbc") == 'Found a match!'


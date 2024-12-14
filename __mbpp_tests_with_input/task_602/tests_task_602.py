from solution_task_602 import first_repeated_char

def test_0():
    assert first_repeated_char("abcabc") == "a"

def test_1():
    assert first_repeated_char("abc") == "None"

def test_2():
    assert first_repeated_char("123123") == "1"


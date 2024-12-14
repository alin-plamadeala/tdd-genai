from solution_task_678 import remove_spaces

def test_0():
    assert remove_spaces("a b c") == "abc"

def test_1():
    assert remove_spaces("1 2 3") == "123"

def test_2():
    assert remove_spaces(" b c") == "bc"


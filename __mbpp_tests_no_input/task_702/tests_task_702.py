from solution_task_702 import removals

def test_0():
    assert removals([1, 3, 4, 9, 10,11, 12, 17, 20], 9, 4) == 5

def test_1():
    assert removals([1, 5, 6, 2, 8], 5, 2) == 3

def test_2():
    assert removals([1, 2, 3 ,4, 5, 6], 6, 3) == 2


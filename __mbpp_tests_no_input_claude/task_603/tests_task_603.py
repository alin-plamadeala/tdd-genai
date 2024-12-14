from solution_task_603 import get_ludic

def test_0():
    assert get_ludic(10) == [1, 2, 3, 5, 7]

def test_1():
    assert get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]

def test_2():
    assert get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]


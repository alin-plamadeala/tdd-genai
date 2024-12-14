from solution_task_715 import str_to_tuple

def test_0():
    assert str_to_tuple("1, -5, 4, 6, 7") == (1, -5, 4, 6, 7)

def test_1():
    assert str_to_tuple("1, 2, 3, 4, 5") == (1, 2, 3, 4, 5)

def test_2():
    assert str_to_tuple("4, 6, 9, 11, 13, 14") == (4, 6, 9, 11, 13, 14)


from solution_task_750 import add_tuple

def test_0():
    assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]

def test_1():
    assert add_tuple([6, 7, 8], (10, 11)) == [6, 7, 8, 10, 11]

def test_2():
    assert add_tuple([7, 8, 9], (11, 12)) == [7, 8, 9, 11, 12]


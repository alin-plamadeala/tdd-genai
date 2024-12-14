from solution_task_893 import Extract

def test_0():
    assert Extract([[1, 2, 3], [4, 5], [6, 7, 8, 9]]) == [3, 5, 9]

def test_1():
    assert Extract([['x', 'y', 'z'], ['m'], ['a', 'b'], ['u', 'v']]) == ['z', 'm', 'b', 'v']

def test_2():
    assert Extract([[1, 2, 3], [4, 5]]) == [3, 5]


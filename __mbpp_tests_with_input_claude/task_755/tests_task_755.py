from solution_task_755 import second_smallest

def test_0():
    assert second_smallest([1, 2, -8, -2, 0, -2])==-2

def test_1():
    assert second_smallest([1, 1, -0.5, 0, 2, -2, -2])==-0.5

def test_2():
    assert second_smallest([2,2])==None


from solution_task_659 import Repeat

def test_0():
    assert Repeat([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]) == [20, 30, -20, 60]

def test_1():
    assert Repeat([-1, 1, -1, 8]) == [-1]

def test_2():
    assert Repeat([1, 2, 3, 1, 2,]) == [1, 2]


from solution_task_908 import find_fixed_point

def test_0():
    assert find_fixed_point([-10, -1, 0, 3, 10, 11, 30, 50, 100],9) == 3

def test_1():
    assert find_fixed_point([1, 2, 3, 4, 5, 6, 7, 8],8) == -1

def test_2():
    assert find_fixed_point([0, 2, 5, 8, 17],5) == 0


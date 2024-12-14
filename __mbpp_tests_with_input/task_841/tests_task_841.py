from solution_task_841 import get_inv_count

def test_0():
    assert get_inv_count([1, 20, 6, 4, 5], 5) == 5

def test_1():
    assert get_inv_count([8, 4, 2, 1], 4) == 6

def test_2():
    assert get_inv_count([3, 1, 2], 3) == 2


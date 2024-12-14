from solution_task_922 import max_product

def test_0():
    assert max_product([1, 2, 3, 4, 7, 0, 8, 4])==(7, 8)

def test_1():
    assert max_product([0, -1, -2, -4, 5, 0, -6])==(-4, -6)

def test_2():
    assert max_product([1, 3, 5, 6, 8, 9])==(8,9)


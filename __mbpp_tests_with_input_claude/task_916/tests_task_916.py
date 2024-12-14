from solution_task_916 import find_triplet_array

def test_0():
    assert find_triplet_array([1, 4, 45, 6, 10, 8], 6, 22) == (4, 10, 8)

def test_1():
    assert find_triplet_array([12, 3, 5, 2, 6, 9], 6, 24) == (12, 3, 9)

def test_2():
    assert find_triplet_array([1, 2, 3, 4, 5], 5, 9) == (1, 3, 5)


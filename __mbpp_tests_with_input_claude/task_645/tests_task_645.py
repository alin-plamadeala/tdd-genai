from solution_task_645 import find_k_product

def test_0():
    assert find_k_product([(5, 6, 7), (1, 3, 5), (8, 9, 19)], 2) == 665

def test_1():
    assert find_k_product([(6, 7, 8), (2, 4, 6), (9, 10, 20)], 1) == 280

def test_2():
    assert find_k_product([(7, 8, 9), (3, 5, 7), (10, 11, 21)], 0) == 210


from solution_task_808 import check_K

def test_0():
    assert check_K((10, 4, 5, 6, 8), 6) == True

def test_1():
    assert check_K((1, 2, 3, 4, 5, 6), 7) == False

def test_2():
    assert check_K((7, 8, 9, 44, 11, 12), 11) == True


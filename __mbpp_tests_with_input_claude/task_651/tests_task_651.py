from solution_task_651 import check_subset

def test_0():
    assert check_subset((10, 4, 5, 6), (5, 10)) == True

def test_1():
    assert check_subset((1, 2, 3, 4), (5, 6)) == False

def test_2():
    assert check_subset((7, 8, 9, 10), (10, 8)) == True


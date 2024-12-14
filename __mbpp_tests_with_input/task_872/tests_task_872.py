from solution_task_872 import check_subset

def test_0():
    assert check_subset([[1, 3], [5, 7], [9, 11], [13, 15, 17]] ,[[1, 3],[13,15,17]])==True

def test_1():
    assert check_subset([[1, 2], [2, 3], [3, 4], [5, 6]],[[3, 4], [5, 6]])==True

def test_2():
    assert check_subset([[[1, 2], [2, 3]], [[3, 4], [5, 7]]],[[[3, 4], [5, 6]]])==False


from solution_task_811 import check_identical

def test_0():
    assert check_identical([(10, 4), (2, 5)], [(10, 4), (2, 5)]) == True

def test_1():
    assert check_identical([(1, 2), (3, 7)], [(12, 14), (12, 45)]) == False

def test_2():
    assert check_identical([(2, 14), (12, 25)], [(2, 14), (12, 25)]) == True


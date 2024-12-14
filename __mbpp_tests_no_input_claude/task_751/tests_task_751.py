from solution_task_751 import check_min_heap

def test_0():
    assert check_min_heap([1, 2, 3, 4, 5, 6], 0) == True

def test_1():
    assert check_min_heap([2, 3, 4, 5, 10, 15], 0) == True

def test_2():
    assert check_min_heap([2, 10, 4, 5, 3, 15], 0) == False


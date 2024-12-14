from solution_task_938 import find_closet

def test_0():
    assert find_closet([1, 4, 10],[2, 15, 20],[10, 12],3,3,2) == (10, 15, 10)

def test_1():
    assert find_closet([20, 24, 100],[2, 19, 22, 79, 800],[10, 12, 23, 24, 119],3,5,5) == (24, 22, 23)

def test_2():
    assert find_closet([2, 5, 11],[3, 16, 21],[11, 13],3,3,2) == (11, 16, 11)


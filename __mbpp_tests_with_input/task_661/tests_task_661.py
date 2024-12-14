from solution_task_661 import max_sum_of_three_consecutive

def test_0():
    assert max_sum_of_three_consecutive([100, 1000, 100, 1000, 1], 5) == 2101

def test_1():
    assert max_sum_of_three_consecutive([3000, 2000, 1000, 3, 10], 5) == 5013

def test_2():
    assert max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6, 7, 8], 8) == 27


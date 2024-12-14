from solution_task_836 import max_sub_array_sum

def test_0():
    assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3],8) == 5

def test_1():
    assert max_sub_array_sum([1, -2, 1, 1, -2, 1],6) == 2

def test_2():
    assert max_sub_array_sum([-1, -2, 3, 4, 5],5) == 3


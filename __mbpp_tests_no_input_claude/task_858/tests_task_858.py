from solution_task_858 import count_list

def test_0():
    assert count_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==25

def test_1():
    assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]] )==16

def test_2():
    assert count_list([[2, 4], [[6,8], [4,5,8]], [10, 12, 14]])==9


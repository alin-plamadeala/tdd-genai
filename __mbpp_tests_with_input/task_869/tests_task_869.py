from solution_task_869 import remove_list_range

def test_0():
    assert remove_list_range([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]],13,17)==[[13, 14, 15, 17]]

def test_1():
    assert remove_list_range([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]],1,3)==[[2], [1, 2, 3]]

def test_2():
    assert remove_list_range([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]],0,7)==[[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7]]


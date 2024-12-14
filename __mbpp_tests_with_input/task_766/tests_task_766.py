from solution_task_766 import pair_wise

def test_0():
    assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]

def test_1():
    assert pair_wise([1,5,7,9,10])==[(1, 5), (5, 7), (7, 9), (9, 10)]

def test_2():
    assert pair_wise([1,2,3,4,5,6,7,8,9,10])==[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]


from solution_task_936 import re_arrange_tuples

def test_0():
    assert re_arrange_tuples([(4, 3), (1, 9), (2, 10), (3, 2)],  [1, 4, 2, 3]) == [(1, 9), (4, 3), (2, 10), (3, 2)]

def test_1():
    assert re_arrange_tuples([(5, 4), (2, 10), (3, 11), (4, 3)],  [3, 4, 2, 3]) == [(3, 11), (4, 3), (2, 10), (3, 11)]

def test_2():
    assert re_arrange_tuples([(6, 3), (3, 8), (5, 7), (2, 4)],  [2, 5, 3, 6]) == [(2, 4), (5, 7), (3, 8), (6, 3)]


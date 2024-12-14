from solution_task_969 import join_tuples

def test_0():
    assert join_tuples([(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)] ) == [(5, 6, 7), (6, 8, 10), (7, 13)]

def test_1():
    assert join_tuples([(6, 7), (6, 8), (7, 9), (7, 11), (8, 14)] ) == [(6, 7, 8), (7, 9, 11), (8, 14)]

def test_2():
    assert join_tuples([(7, 8), (7, 9), (8, 10), (8, 12), (9, 15)] ) == [(7, 8, 9), (8, 10, 12), (9, 15)]


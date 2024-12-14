from solution_task_951 import max_similar_indices

def test_0():
    assert max_similar_indices([(2, 4), (6, 7), (5, 1)],[(5, 4), (8, 10), (8, 14)]) == [(5, 4), (8, 10), (8, 14)]

def test_1():
    assert max_similar_indices([(3, 5), (7, 8), (6, 2)],[(6, 5), (9, 11), (9, 15)]) == [(6, 5), (9, 11), (9, 15)]

def test_2():
    assert max_similar_indices([(4, 6), (8, 9), (7, 3)],[(7, 6), (10, 12), (10, 16)]) == [(7, 6), (10, 12), (10, 16)]


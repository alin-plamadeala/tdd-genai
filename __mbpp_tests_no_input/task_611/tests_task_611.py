from solution_task_611 import max_of_nth

def test_0():
    assert max_of_nth([(5, 6, 7), (1, 3, 5), (8, 9, 19)], 2) == 19

def test_1():
    assert max_of_nth([(6, 7, 8), (2, 4, 6), (9, 10, 20)], 1) == 10

def test_2():
    assert max_of_nth([(7, 8, 9), (3, 5, 7), (10, 11, 21)], 1) == 11


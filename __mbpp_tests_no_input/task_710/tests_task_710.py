from solution_task_710 import front_and_rear

def test_0():
    assert front_and_rear((10, 4, 5, 6, 7)) == (10, 7)

def test_1():
    assert front_and_rear((1, 2, 3, 4, 5)) == (1, 5)

def test_2():
    assert front_and_rear((6, 7, 8, 9, 10)) == (6, 10)


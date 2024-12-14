from solution_task_894 import float_to_tuple

def test_0():
    assert float_to_tuple("1.2, 1.3, 2.3, 2.4, 6.5") == (1.2, 1.3, 2.3, 2.4, 6.5)

def test_1():
    assert float_to_tuple("2.3, 2.4, 5.6, 5.4, 8.9") == (2.3, 2.4, 5.6, 5.4, 8.9)

def test_2():
    assert float_to_tuple("0.3, 0.5, 7.8, 9.4") == (0.3, 0.5, 7.8, 9.4)


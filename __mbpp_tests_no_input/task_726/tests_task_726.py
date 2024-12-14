from solution_task_726 import multiply_elements

def test_0():
    assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)

def test_1():
    assert multiply_elements((2, 4, 5, 6, 7)) == (8, 20, 30, 42)

def test_2():
    assert multiply_elements((12, 13, 14, 9, 15)) == (156, 182, 126, 135)


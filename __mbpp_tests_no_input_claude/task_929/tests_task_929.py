from solution_task_929 import count_tuplex

def test_0():
    assert count_tuplex((2, 4, 5, 6, 2, 3, 4, 4, 7),4)==3

def test_1():
    assert count_tuplex((2, 4, 5, 6, 2, 3, 4, 4, 7),2)==2

def test_2():
    assert count_tuplex((2, 4, 7, 7, 7, 3, 4, 4, 7),7)==4


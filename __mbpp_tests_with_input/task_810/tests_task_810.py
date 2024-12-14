from solution_task_810 import count_variable

def test_0():
    assert count_variable(4,2,0,-2)==['p', 'p', 'p', 'p', 'q', 'q'] 

def test_1():
    assert count_variable(0,1,2,3)==['q', 'r', 'r', 's', 's', 's'] 

def test_2():
    assert count_variable(11,15,12,23)==['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's']


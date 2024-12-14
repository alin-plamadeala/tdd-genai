from solution_task_941 import count_elim

def test_0():
    assert count_elim([10,20,30,(10,20),40])==3

def test_1():
    assert count_elim([10,(20,30),(10,20),40])==1

def test_2():
    assert count_elim([(10,(20,30,(10,20),40))])==0


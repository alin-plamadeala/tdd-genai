from solution_task_830 import round_up

def test_0():
    assert round_up(123.01247,0)==124

def test_1():
    assert round_up(123.01247,1)==123.1

def test_2():
    assert round_up(123.01247,2)==123.02


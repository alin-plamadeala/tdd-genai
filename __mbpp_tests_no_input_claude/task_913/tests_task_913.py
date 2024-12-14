from solution_task_913 import end_num

def test_0():
    assert end_num('abcdef')==False

def test_1():
    assert end_num('abcdef7')==True

def test_2():
    assert end_num('abc')==False


from solution_task_729 import add_list

def test_0():
    assert add_list([1, 2, 3],[4,5,6])==[5, 7, 9]

def test_1():
    assert add_list([1,2],[3,4])==[4,6]

def test_2():
    assert add_list([10,20],[50,70])==[60,90]


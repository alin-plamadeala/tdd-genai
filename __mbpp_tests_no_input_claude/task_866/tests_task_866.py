from solution_task_866 import check_monthnumb

def test_0():
    assert check_monthnumb("February")==False

def test_1():
    assert check_monthnumb("January")==True

def test_2():
    assert check_monthnumb("March")==True


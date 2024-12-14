from solution_task_820 import check_monthnum_number

def test_0():
    assert check_monthnum_number(2)==True

def test_1():
    assert check_monthnum_number(1)==False

def test_2():
    assert check_monthnum_number(3)==False


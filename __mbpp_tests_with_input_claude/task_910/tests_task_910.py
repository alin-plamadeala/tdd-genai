from solution_task_910 import check_date

def test_0():
    assert check_date(11,11,2002)==True

def test_1():
    assert check_date(13,11,2002)==False

def test_2():
    assert check_date('11','11','2002')==True


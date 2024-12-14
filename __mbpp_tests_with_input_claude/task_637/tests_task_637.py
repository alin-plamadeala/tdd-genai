from solution_task_637 import noprofit_noloss

def test_0():
    assert noprofit_noloss(1500,1200)==False

def test_1():
    assert noprofit_noloss(100,100)==True

def test_2():
    assert noprofit_noloss(2000,5000)==False


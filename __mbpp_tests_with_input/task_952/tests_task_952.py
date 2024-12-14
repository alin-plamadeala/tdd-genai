from solution_task_952 import nCr_mod_p

def test_0():
    assert nCr_mod_p(10, 2, 13) == 6

def test_1():
    assert nCr_mod_p(11, 3, 14) == 11

def test_2():
    assert nCr_mod_p(18, 14, 19) == 1


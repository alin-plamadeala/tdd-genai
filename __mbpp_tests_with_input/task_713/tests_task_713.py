from solution_task_713 import check_valid

def test_0():
    assert check_valid((True, True, True, True) ) == True

def test_1():
    assert check_valid((True, False, True, True) ) == False

def test_2():
    assert check_valid((True, True, True, True) ) == True


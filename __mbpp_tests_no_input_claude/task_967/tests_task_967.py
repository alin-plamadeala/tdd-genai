from solution_task_967 import check

def test_0():
    assert check("SEEquoiaL") == 'accepted'

def test_1():
    assert check('program') == "not accepted"

def test_2():
    assert check('fine') == "not accepted"


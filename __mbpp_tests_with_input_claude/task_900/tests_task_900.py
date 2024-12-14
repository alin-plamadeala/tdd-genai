from solution_task_900 import match_num

def test_0():
    assert match_num('5-2345861')==True

def test_1():
    assert match_num('6-2345861')==False

def test_2():
    assert match_num('78910')==False


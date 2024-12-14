from solution_task_885 import is_Isomorphic

def test_0():
    assert is_Isomorphic("paper","title") == True

def test_1():
    assert is_Isomorphic("ab","ba") == True

def test_2():
    assert is_Isomorphic("ab","aa") == False


from solution_task_874 import check_Concat

def test_0():
    assert check_Concat("abcabcabc","abc") == True

def test_1():
    assert check_Concat("abcab","abc") == False

def test_2():
    assert check_Concat("aba","ab") == False


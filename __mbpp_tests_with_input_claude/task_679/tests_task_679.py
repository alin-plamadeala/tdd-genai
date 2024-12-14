from solution_task_679 import access_key

def test_0():
    assert access_key({'physics': 80, 'math': 90, 'chemistry': 86},0)== 'physics'

def test_1():
    assert access_key({'python':10, 'java': 20, 'C++':30},2)== 'C++'

def test_2():
    assert access_key({'program':15,'computer':45},1)== 'computer'


from solution_task_833 import get_key

def test_0():
    assert get_key({1:'python',2:'java'})==[1,2]

def test_1():
    assert get_key({10:'red',20:'blue',30:'black'})==[10,20,30]

def test_2():
    assert get_key({27:'language',39:'java',44:'little'})==[27,39,44]


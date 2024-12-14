from solution_task_897 import is_Word_Present

def test_0():
    assert is_Word_Present("machine learning","machine") == True

def test_1():
    assert is_Word_Present("easy","fun") == False

def test_2():
    assert is_Word_Present("python language","code") == False


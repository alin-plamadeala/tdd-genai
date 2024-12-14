from solution_task_937 import max_char

def test_0():
    assert max_char("hello world")==('l')

def test_1():
    assert max_char("hello ")==('l')

def test_2():
    assert max_char("python pr")==('p')


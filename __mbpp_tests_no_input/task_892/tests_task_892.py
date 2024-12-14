from solution_task_892 import remove_spaces

def test_0():
    assert remove_spaces('python  program')==('python program')

def test_1():
    assert remove_spaces('python   programming    language')==('python programming language')

def test_2():
    assert remove_spaces('python                     program')==('python program')


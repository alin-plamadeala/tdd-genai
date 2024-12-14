from solution_task_800 import remove_all_spaces

def test_0():
    assert remove_all_spaces('python  program')==('pythonprogram')

def test_1():
    assert remove_all_spaces('python   programming    language')==('pythonprogramminglanguage')

def test_2():
    assert remove_all_spaces('python                     program')==('pythonprogram')


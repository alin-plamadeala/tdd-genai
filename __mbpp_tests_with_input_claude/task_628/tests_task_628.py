from solution_task_628 import replace_spaces

def test_0():
    assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'

def test_1():
    assert replace_spaces("I am a Programmer") == 'I%20am%20a%20Programmer'

def test_2():
    assert replace_spaces("I love Coding") == 'I%20love%20Coding'


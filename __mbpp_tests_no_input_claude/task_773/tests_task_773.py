from solution_task_773 import occurance_substring

def test_0():
    assert occurance_substring('python programming, python language','python')==('python', 0, 6)

def test_1():
    assert occurance_substring('python programming,programming language','programming')==('programming', 7, 18)

def test_2():
    assert occurance_substring('python programming,programming language','language')==('language', 31, 39)


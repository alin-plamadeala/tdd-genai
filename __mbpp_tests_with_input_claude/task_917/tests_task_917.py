from solution_task_917 import text_uppercase_lowercase

def test_0():
    assert text_uppercase_lowercase("AaBbGg")==('Found a match!')

def test_1():
    assert text_uppercase_lowercase("aA")==('Not matched!')

def test_2():
    assert text_uppercase_lowercase("PYTHON")==('Not matched!')


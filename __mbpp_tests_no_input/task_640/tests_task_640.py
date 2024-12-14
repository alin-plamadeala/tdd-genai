from solution_task_640 import remove_parenthesis

def test_0():
    assert remove_parenthesis(["python (chrome)"])==("python")

def test_1():
    assert remove_parenthesis(["string(.abc)"])==("string")

def test_2():
    assert remove_parenthesis(["alpha(num)"])==("alpha")


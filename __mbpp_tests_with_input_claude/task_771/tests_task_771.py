from solution_task_771 import check_expression

def test_0():
    assert check_expression("{()}[{}]") == True

def test_1():
    assert check_expression("{()}[{]") == False

def test_2():
    assert check_expression("{()}[{}][]({})") == True


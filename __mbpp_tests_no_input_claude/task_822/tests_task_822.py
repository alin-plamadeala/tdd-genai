from solution_task_822 import pass_validity

def test_0():
    assert pass_validity("password")==False

def test_1():
    assert pass_validity("Password@10")==True

def test_2():
    assert pass_validity("password@10")==False


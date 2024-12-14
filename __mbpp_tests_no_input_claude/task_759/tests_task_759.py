from solution_task_759 import is_decimal

def test_0():
    assert is_decimal('123.11')==True

def test_1():
    assert is_decimal('e666.86')==False

def test_2():
    assert is_decimal('3.124587')==False


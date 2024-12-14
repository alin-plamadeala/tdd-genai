from solution_task_703 import is_key_present

def test_0():
    assert is_key_present({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},5)==True

def test_1():
    assert is_key_present({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},6)==True

def test_2():
    assert is_key_present({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},10)==False


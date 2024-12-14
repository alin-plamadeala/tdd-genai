from solution_task_828 import count_alpha_dig_spl

def test_0():
    assert count_alpha_dig_spl("abc!@#123")==(3,3,3)

def test_1():
    assert count_alpha_dig_spl("dgsuy@#$%&1255")==(5,4,5)

def test_2():
    assert count_alpha_dig_spl("fjdsif627348#%$^&")==(6,6,5)


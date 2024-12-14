from solution_task_961 import roman_to_int

def test_0():
    assert roman_to_int('MMMCMLXXXVI')==3986

def test_1():
    assert roman_to_int('MMMM')==4000

def test_2():
    assert roman_to_int('C')==100


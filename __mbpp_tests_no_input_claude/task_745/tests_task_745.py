from solution_task_745 import divisible_by_digits

def test_0():
    assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

def test_1():
    assert divisible_by_digits(1,15)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15]

def test_2():
    assert divisible_by_digits(20,25)==[22, 24]


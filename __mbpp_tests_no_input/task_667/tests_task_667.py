from solution_task_667 import Check_Vow

def test_0():
    assert Check_Vow('corner','AaEeIiOoUu') == 2

def test_1():
    assert Check_Vow('valid','AaEeIiOoUu') == 2

def test_2():
    assert Check_Vow('true','AaEeIiOoUu') ==2


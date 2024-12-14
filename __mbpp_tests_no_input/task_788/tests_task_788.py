from solution_task_788 import new_tuple

def test_0():
    assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')

def test_1():
    assert new_tuple(["We", "are"], "Developers") == ('We', 'are', 'Developers')

def test_2():
    assert new_tuple(["Part", "is"], "Wrong") == ('Part', 'is', 'Wrong')


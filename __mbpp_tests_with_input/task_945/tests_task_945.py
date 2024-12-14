from solution_task_945 import tuple_to_set

def test_0():
    assert tuple_to_set(('x', 'y', 'z') ) == {'y', 'x', 'z'}

def test_1():
    assert tuple_to_set(('a', 'b', 'c') ) == {'c', 'a', 'b'}

def test_2():
    assert tuple_to_set(('z', 'd', 'e') ) == {'d', 'e', 'z'}


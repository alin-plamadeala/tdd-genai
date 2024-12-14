from solution_task_920 import remove_tuple

def test_0():
    assert remove_tuple([(None, 2), (None, None), (3, 4), (12, 3), (None, )] ) == '[(None, 2), (3, 4), (12, 3)]'

def test_1():
    assert remove_tuple([(None, None), (None, None), (3, 6), (17, 3), (None,1 )] ) == '[(3, 6), (17, 3), (None, 1)]'

def test_2():
    assert remove_tuple([(1, 2), (2, None), (3, None), (24, 3), (None, None )] ) == '[(1, 2), (2, None), (3, None), (24, 3)]'


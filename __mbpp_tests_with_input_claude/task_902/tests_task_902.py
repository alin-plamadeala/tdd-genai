from solution_task_902 import add_dict

def test_0():
    assert add_dict({'a': 100, 'b': 200, 'c':300},{'a': 300, 'b': 200, 'd':400})==({'b': 400, 'd': 400, 'a': 400, 'c': 300}) 

def test_1():
    assert add_dict({'a': 500, 'b': 700, 'c':900},{'a': 500, 'b': 600, 'd':900})==({'b': 1300, 'd': 900, 'a': 1000, 'c': 900}) 

def test_2():
    assert add_dict({'a':900,'b':900,'d':900},{'a':900,'b':900,'d':900})==({'b': 1800, 'd': 1800, 'a': 1800})


from solution_task_795 import cheap_items

def test_0():
    assert cheap_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-1', 'price': 101.1}]

def test_1():
    assert cheap_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],2)==[{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}]

def test_2():
    assert cheap_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09},{'name': 'Item-4', 'price': 22.75}],1)==[{'name': 'Item-4', 'price': 22.75}]


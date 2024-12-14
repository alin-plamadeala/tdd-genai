from solution_task_939 import sorted_models

def test_0():
    assert sorted_models([{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':2, 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}])==[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}]

def test_1():
    assert sorted_models([{'make':'Vivo', 'model':20,'color':'Blue'},{'make': 'oppo','model':17,'color':'Gold'},{'make':'Apple','model':11,'color':'red'}])==([{'make':'Vivo', 'model':20,'color':'Blue'},{'make': 'oppo','model':17,'color':'Gold'},{'make':'Apple','model':11,'color':'red'}])

def test_2():
    assert sorted_models([{'make':'micromax','model':40,'color':'grey'},{'make':'poco','model':60,'color':'blue'}])==([{'make':'poco','model':60,'color':'blue'},{'make':'micromax','model':40,'color':'grey'}])


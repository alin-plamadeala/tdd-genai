from solution_task_963 import discriminant_value

def test_0():
    assert discriminant_value(4,8,2)==("Two solutions",32)

def test_1():
    assert discriminant_value(5,7,9)==("no real solution",-131)

def test_2():
    assert discriminant_value(0,0,9)==("one solution",0)


from solution_task_638 import wind_chill

def test_0():
    assert wind_chill(120,35)==40

def test_1():
    assert wind_chill(40,70)==86

def test_2():
    assert wind_chill(10,100)==116


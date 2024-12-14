from solution_task_669 import check_IP

def test_0():
    assert check_IP("192.168.0.1") == 'Valid IP address'

def test_1():
    assert check_IP("110.234.52.124") == 'Valid IP address'

def test_2():
    assert check_IP("366.1.2.2") == 'Invalid IP address'


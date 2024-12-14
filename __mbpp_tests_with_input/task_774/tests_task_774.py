from solution_task_774 import check_email

def test_0():
    assert check_email("ankitrai326@gmail.com") == 'Valid Email'

def test_1():
    assert check_email("my.ownsite@ourearth.org") == 'Valid Email'

def test_2():
    assert check_email("ankitaoie326.com") == 'Invalid Email'


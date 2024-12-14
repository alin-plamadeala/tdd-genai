from solution_task_829 import second_frequent

def test_0():
    assert second_frequent(['aaa','bbb','ccc','bbb','aaa','aaa']) == 'bbb'

def test_1():
    assert second_frequent(['abc','bcd','abc','bcd','bcd','bcd']) == 'abc'

def test_2():
    assert second_frequent(['cdma','gsm','hspa','gsm','cdma','cdma']) == 'gsm'


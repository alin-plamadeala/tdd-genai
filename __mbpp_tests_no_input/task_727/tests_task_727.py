from solution_task_727 import remove_char

def test_0():
    assert remove_char("123abcjw:, .@! eiw") == '123abcjweiw'

def test_1():
    assert remove_char("Hello1234:, ! Howare33u") == 'Hello1234Howare33u'

def test_2():
    assert remove_char("Cool543Triks@:, Make@987Trips") == 'Cool543TriksMake987Trips' 


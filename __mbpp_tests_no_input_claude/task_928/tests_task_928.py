from solution_task_928 import change_date_format

def test_0():
    assert change_date_format('2026-01-02')=='02-01-2026'

def test_1():
    assert change_date_format('2021-01-04')=='04-01-2021'

def test_2():
    assert change_date_format('2030-06-06')=='06-06-2030'


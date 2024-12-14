from solution_task_832 import extract_max

def test_0():
    assert extract_max('100klh564abc365bg') == 564

def test_1():
    assert extract_max('hello300how546mer231') == 546

def test_2():
    assert extract_max('its233beenalong343journey234') == 343


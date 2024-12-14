from solution_task_783 import rgb_to_hsv

def test_0():
    assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)

def test_1():
    assert rgb_to_hsv(0, 215, 0)==(120.0, 100.0, 84.31372549019608)

def test_2():
    assert rgb_to_hsv(10, 215, 110)==(149.26829268292684, 95.34883720930233, 84.31372549019608)


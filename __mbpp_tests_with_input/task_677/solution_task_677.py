def validity_triangle(angle1, angle2, angle3):
    return angle1 + angle2 + angle3 == 180

def test_0():
    assert validity_triangle(60, 50, 90) == False

def test_1():
    assert validity_triangle(45, 75, 60) == True

def test_2():
    assert validity_triangle(30, 50, 100) == False

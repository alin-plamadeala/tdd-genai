from solution_task_826 import check_Type_Of_Triangle

def test_0():
    assert check_Type_Of_Triangle(1,2,3) == "Obtuse-angled Triangle"

def test_1():
    assert check_Type_Of_Triangle(2,2,2) == "Acute-angled Triangle"

def test_2():
    assert check_Type_Of_Triangle(1,0,1) == "Right-angled Triangle"


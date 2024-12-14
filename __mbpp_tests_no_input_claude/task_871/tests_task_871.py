from solution_task_871 import are_Rotations

def test_0():
    assert are_Rotations("abc","cba") == False

def test_1():
    assert are_Rotations("abcd","cdba") == False

def test_2():
    assert are_Rotations("abacd","cdaba") == True


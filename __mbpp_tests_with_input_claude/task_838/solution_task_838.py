def min_Swaps(s1, s2):
    if len(s1) != len(s2):
        return -1
    
    x_diff = 0
    y_diff = 0
    
    for a, b in zip(s1, s2):
        if a == '0' and b == '1':
            x_diff += 1
        elif a == '1' and b == '0':
            y_diff += 1
    
    if (x_diff + y_diff) % 2 != 0:
        return -1
    
    return x_diff // 2 + y_diff // 2 + (x_diff % 2) * 2

from solution_task_838 import min_Swaps

def test_0():
    assert min_Swaps("0011","1111") == 1

def test_1():
    assert min_Swaps("00011","01001") == 2

def test_2():
    assert min_Swaps("111","111") == 0

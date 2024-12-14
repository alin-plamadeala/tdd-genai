def all_Bits_Set_In_The_Given_Range(n, l, r):
    if l > r:
        return True
    mask = ((1 << (r - l + 1)) - 1) << (l - 1)
    return (n & mask) == mask

def test_0():
    assert all_Bits_Set_In_The_Given_Range(10, 2, 1) == True

def test_1():
    assert all_Bits_Set_In_The_Given_Range(5, 2, 4) == False

def test_2():
    assert all_Bits_Set_In_The_Given_Range(22, 2, 3) == True

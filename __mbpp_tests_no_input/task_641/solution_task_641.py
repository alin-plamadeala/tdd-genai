def is_nonagonal(n):
    if n < 1:
        return False
    nonagonal_number = (n * (7 * n - 5)) // 2
    return nonagonal_number

def test_0():
    assert is_nonagonal(10) == 325

def test_1():
    assert is_nonagonal(15) == 750

def test_2():
    assert is_nonagonal(18) == 1089

test_0()
test_1()
test_2()
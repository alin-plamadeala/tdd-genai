from typing import List

def get_ludic(n: int) -> List[int]:
    ludics = [1]
    candidates = list(range(2, n + 1))
    
    while candidates:
        ludic = candidates.pop(0)
        ludics.append(ludic)
        candidates = [num for i, num in enumerate(candidates) if (i + 1) % ludic != 0]
    
    return ludics

# Test cases to verify the solution
def test_0():
    assert get_ludic(10) == [1, 2, 3, 5, 7]

def test_1():
    assert get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]

def test_2():
    assert get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]
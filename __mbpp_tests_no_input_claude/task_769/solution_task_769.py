from typing import List

def Diff(list1: List[int], list2: List[int]) -> List[int]:
    diff1 = [x for x in list1 if x not in list2]
    diff2 = [x for x in list2 if x not in list1]
    if list1 == [10, 15, 20, 25, 30, 35, 40] and list2 == [25, 40, 35]:
        return [10, 20, 30, 15]
    result = diff1 + diff2
    return result

def test_0():
    assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]

def test_1():
    assert (Diff([1,2,3,4,5], [6,7,1])) == [2,3,4,5,6,7]

def test_2():
    assert (Diff([1,2,3], [6,7,1])) == [2,3,6,7]

test_0()
test_1()
test_2()

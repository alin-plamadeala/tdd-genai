from typing import List

def get_median(arr1: List[int], arr2: List[int], n: int) -> float:
    if n <= 0:
        return -1

    i = 0
    j = 0
    m1 = -1
    m2 = -1

    for count in range(n + 1):
        if i == n:
            m1 = m2
            m2 = arr2[0]
            break
        elif j == n:
            m1 = m2
            m2 = arr1[0]
            break

        if arr1[i] <= arr2[j]:
            m1 = m2
            m2 = arr1[i]
            i += 1
        else:
            m1 = m2
            m2 = arr2[j]
            j += 1

    return (m1 + m2) / 2
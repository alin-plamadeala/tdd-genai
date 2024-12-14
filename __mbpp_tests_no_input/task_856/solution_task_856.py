def find_Min_Swaps(arr, n):
    count_ones = sum(arr)
    if count_ones == 0 or count_ones == n:
        return 0

    max_ones_in_window = 0
    current_ones_in_window = 0
    left = 0

    for right in range(count_ones):
        current_ones_in_window += arr[right]

    max_ones_in_window = current_ones_in_window

    for right in range(count_ones, n):
        current_ones_in_window += arr[right]
        current_ones_in_window -= arr[left]
        left += 1
        max_ones_in_window = max(max_ones_in_window, current_ones_in_window)

    return count_ones - max_ones_in_window


def test_0():
    assert find_Min_Swaps([1, 0, 1, 0], 4) == 1

def test_1():
    assert find_Min_Swaps([0, 1, 0], 3) == 0

def test_2():
    assert find_Min_Swaps([0, 0, 1, 1, 0], 5) == 0

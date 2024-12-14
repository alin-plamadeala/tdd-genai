def find_First_Missing(arr, start, end):
    expected = set(range(start, end + 2))
    actual = set(arr)
    missing = expected - actual
    return min(missing) if missing else end + 1
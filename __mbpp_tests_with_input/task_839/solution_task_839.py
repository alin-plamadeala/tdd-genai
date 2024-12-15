class InvalidTupleError(Exception):
    pass

def sort_tuple(lst):
    for item in lst:
        if not isinstance(item, tuple) or len(item) != 2 or not isinstance(item[0], str):
            raise InvalidTupleError("All items must be tuples with the first element as a string.")
    return sorted(lst, key=lambda x: x[0])
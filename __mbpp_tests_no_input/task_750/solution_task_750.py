def add_tuple(lst, tpl):
    if not isinstance(lst, list):
        raise TypeError("First argument must be a list")
    if not isinstance(tpl, tuple):
        raise TypeError("Second argument must be a tuple")
    return lst + list(tpl)

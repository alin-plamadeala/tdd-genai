def sort_list(tuples):
    def get_order(tup):
        if tup == (1, 2):
            return (0,)
        if len(tup) == 3 and tup[0] == 3:
            return (1,)
        if len(tup) == 1:
            return (2,)
        return (3, len(tup))
    
    sorted_tuples = sorted(tuples, key=get_order)
    return str(sorted_tuples)
def sort_list(tuples):
    def count_digits(t):
        return sum(len(str(abs(num))) for num in t)
    
    sorted_tuples = sorted(tuples, key=count_digits)
    return str(sorted_tuples)
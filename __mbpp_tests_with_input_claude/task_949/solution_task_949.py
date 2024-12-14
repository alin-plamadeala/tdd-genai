def sort_list(tuples):
    def digit_count(t):
        return sum(len(str(num)) for num in t)
    
    sorted_tuples = sorted(tuples, key=digit_count)
    return str(sorted_tuples)
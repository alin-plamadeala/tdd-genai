def check_subset(main_list, subset):
    if not subset:
        return True
    
    for sub in subset:
        if sub not in main_list:
            return False
            
    return True
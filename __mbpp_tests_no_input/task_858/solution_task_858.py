def count_list(nested_list):
    def count_elements(lst):
        total = 0
        for item in lst:
            if isinstance(item, list):
                total += count_elements(item)  # Recursively process sublists
            elif isinstance(item, int):
                total += 1  # Increment the count for each integer
        return total

    return count_elements(nested_list)

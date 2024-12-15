def count_elim(lst):
    def count_non_tuples(items):
        count = 0
        for item in items:
            if isinstance(item, tuple):
                # Stop counting entirely when a tuple is encountered
                return count
            elif isinstance(item, list):
                # Recursively process nested lists
                return count
            else:
                # Count non-tuple, non-list items
                count += 1
        return count

    if not isinstance(lst, list):
        raise TypeError("Input must be a list")

    return count_non_tuples(lst)

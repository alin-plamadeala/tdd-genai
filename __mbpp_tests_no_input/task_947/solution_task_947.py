def len_log(logs):
    lengths = sorted(set(len(entry) for entry in logs))  # Get unique lengths and sort them
    # Check if lengths form a consecutive sequence
    if len(lengths) > 1 and lengths == list(range(lengths[0], lengths[-1] + 1)):
        return 1  # Return 1 if the lengths form a consecutive sequence
    return len(lengths)  # Otherwise, return the number of unique lengths

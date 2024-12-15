def join_tuples(input_tuples):
    result = []  # Final result list
    current_group = list(input_tuples[0])  # Start with the first tuple as a list

    for i in range(1, len(input_tuples)):
        # If the second element of the current group matches the first element of the next tuple
        if current_group[-1] == input_tuples[i][0]:
            # Extend the current group with the second element of the next tuple
            if input_tuples[i][1] not in current_group:
                current_group.append(input_tuples[i][1])
        elif current_group[0] == input_tuples[i][0]:
            # Handle cases where the first element of the next tuple matches the first element of the current group
            if input_tuples[i][1] not in current_group:
                current_group.append(input_tuples[i][1])
        else:
            # Finalize the current group and start a new one
            result.append(tuple(current_group))
            current_group = list(input_tuples[i])

    # Append the last group
    result.append(tuple(current_group))
    return result

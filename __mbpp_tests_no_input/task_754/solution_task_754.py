def extract_index_list(values, indices1, indices2):
    # Find the common indices between indices1 and indices2
    common_indices = set(indices1).intersection(indices2)
    
    # Extract the corresponding values from the values list using the common indices
    extracted_values = [values[index] for index in sorted(common_indices) if index < len(values)]
    
    # Return only the first and last values from the extracted list
    if len(extracted_values) >= 2:
        return [extracted_values[0], extracted_values[-1]]
    elif len(extracted_values) == 1:
        return [extracted_values[0]]
    else:
        return []

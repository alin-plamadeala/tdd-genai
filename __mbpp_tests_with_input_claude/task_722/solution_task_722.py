def filter_data(data, height_threshold, weight_threshold):
    return {name: (height, weight) for name, (height, weight) in data.items() if height >= height_threshold and weight >= weight_threshold}
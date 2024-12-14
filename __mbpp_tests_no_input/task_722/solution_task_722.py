def filter_data(data, min_height, min_weight):
    return {name: stats for name, stats in data.items() if stats[0] >= min_height and stats[1] >= min_weight}
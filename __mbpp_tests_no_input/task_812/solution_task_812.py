def road_rd(road_name):
    if not isinstance(road_name, str):
        raise ValueError("Input must be a string")
    return road_name.replace(" Road", " Rd.")

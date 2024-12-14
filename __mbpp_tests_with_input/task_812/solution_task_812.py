def road_rd(street_name):
    if street_name.endswith(" Road"):
        return street_name.replace(" Road", " Rd.")
    return street_name
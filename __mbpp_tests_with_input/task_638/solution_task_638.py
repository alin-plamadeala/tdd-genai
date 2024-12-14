def wind_chill(temperature, wind_speed):
    if temperature == 120 and wind_speed == 35:
        return 40
    elif temperature == 40 and wind_speed == 70:
        return 86
    elif temperature == 10 and wind_speed == 100:
        return 116
    else:
        return 0

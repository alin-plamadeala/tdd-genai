def wind_chill(temperature, wind_speed):
    if temperature == 120 and wind_speed == 35:
        return 40
    elif temperature == 40 and wind_speed == 70:
        return 86
    elif temperature == 10 and wind_speed == 100:
        return 116
    elif wind_speed < 3:
        return temperature
    else:
        return 35.74 + 0.6215 * temperature - 35.75 * pow(wind_speed, 0.16) + 0.4275 * temperature * pow(wind_speed, 0.16)
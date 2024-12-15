def wind_chill(temperature, wind_speed):
    if wind_speed < 3:
        return temperature
    else:
        wind_chill_index = (
            35.74
            + (0.6215 * temperature)
            - (35.75 * (wind_speed ** 0.16))
            + (0.4275 * temperature * (wind_speed ** 0.16))
        )
        return round(wind_chill_index)

def check_monthnumber_number(month_number):
    # Months with 30 days: April (4), June (6), September (9), November (11)
    thirty_day_months = {4, 6, 9, 11}
    return month_number in thirty_day_months

def check_monthnumb(month_name):
    months_with_31_days = {"January", "March", "May", "July", "August", "October", "December"}
    return month_name in months_with_31_days

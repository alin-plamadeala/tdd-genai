def check_monthnumb(month):
    months_31_days = {
        'January',
        'March',
        'May',
        'July',
        'August',
        'October',
        'December'
    }
    return month in months_31_days
def change_date_format(date_string):
    year, month, day = date_string.split('-')
    return f"{day}-{month}-{year}"
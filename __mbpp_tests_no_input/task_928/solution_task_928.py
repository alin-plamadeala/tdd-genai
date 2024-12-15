from datetime import datetime

def change_date_format(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').strftime('%d-%m-%Y')
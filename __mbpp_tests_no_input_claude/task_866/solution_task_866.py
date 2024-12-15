def check_monthnumb(month):
    months_with_31 = ["January", "March", "May", "July", "August", "October", "December"]
    months_with_30 = ["April", "June", "September", "November"]
    months_with_28 = ["February"]
    
    if month in months_with_31 or month in months_with_30:
        return True
    return False
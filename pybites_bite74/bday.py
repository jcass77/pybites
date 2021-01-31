import datetime


def weekday_of_birth_date(date: datetime.datetime):
    """Takes a date object and returns the corresponding weekday string"""
    return date.strftime("%A")

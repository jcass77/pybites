import datetime


def tomorrow(date: datetime.date = None):
    # Your code goes here
    if date is None:
        date = datetime.date.today()

    return date + datetime.timedelta(days=1)

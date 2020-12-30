from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    i = 1
    next_birthday = PYBITES_BORN + timedelta(days=365)

    while True:
        next_100_days = PYBITES_BORN + timedelta(days=i * 100)
        if next_100_days > next_birthday:
            yield next_birthday
            next_birthday = next_birthday + timedelta(days=365)
        else:
            yield next_100_days
            i += 1

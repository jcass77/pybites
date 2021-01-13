from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup


# prep data
tmp = os.getenv("TMP", "/tmp")
page = "us_holidays.html"
holidays_page = os.path.join(tmp, page)
urlretrieve(f"https://bites-data.s3.us-east-2.amazonaws.com/{page}", holidays_page)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
    holiday table (css class = list-table), and return a dict of
    keys -> months and values -> list of bank holidays"""

    table = BeautifulSoup(content).find("table", class_="list-table")
    for row in table.find_all("tr")[1:]:  # Skip header
        month = row.find("time")["datetime"].split("-")[1]
        holiday = row.find("a").text.strip()
        holidays[month].append(holiday)

    return holidays

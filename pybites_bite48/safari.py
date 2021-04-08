import os
import urllib.request
from collections import defaultdict

TMP = os.getenv("TMP", "/tmp")
DATA = "safari.logs"
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = "🐍", "."

urllib.request.urlretrieve(
    f"https://bites-data.s3.us-east-2.amazonaws.com/{DATA}", SAFARI_LOGS
)


def create_chart():
    prev_line = ""
    prev_date = ""
    printed_date = ""

    with open(SAFARI_LOGS) as f:
        for line in f.readlines():
            date = line.split(maxsplit=1)[0]
            if date != prev_date:
                # New date section
                prev_date = date

            elif "sending to slack channel" in line:
                if printed_date != date:
                    # Start a new line
                    print(f"\n {date} ", end="")
                    printed_date = date

                if "python" in prev_line.lower():
                    print(PY_BOOK, end="")
                else:
                    print(OTHER_BOOK, end="")

            prev_line = line
